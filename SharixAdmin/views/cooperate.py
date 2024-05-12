from datetime import datetime, timedelta

from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin

from SharixAdmin.forms import CompanyForm
from tickets.models import Ticket, TicketList


class CooperateView(UserPassesTestMixin, FormView):
    form_class = CompanyForm
    template_name = "SharixAdmin/cooperate.html"
    success_url = reverse_lazy("cooperate")

    # Проверяем не состояит ли текущий пользователь в группе PARTNER-ADMIN
    def test_func(self):
        return not self.request.user.groups.filter(name='PARTNER-ADMIN').exists()

    def form_valid(self, form):
        # Сохраняем форму, чтобы получить объект компании
        instance = form.save(commit=False)
    
        # Присваиваем полю repr_id идентификатор текущего пользователя
        instance.repr_id = self.request.user

        # Создаем новую запись в БД, чтобы иметь доступ к ID
        instance.save() 

        # Создание тикета на активацию партнера
        # Создаем объект тикета и присваиваем его полю ticket_status
        instance.ticket_status = Ticket.objects.create(
            title=f"Создание нового Партнера '{instance.legal_name}'",
            ticket_list=TicketList.objects.get(pk=2102),# METASERVICE-ADMIN: Права в сервисе (ACCESS_REQUEST)
            ticket_type=3, # ACCESS_REQUEST
            due_date=datetime.now().date() + timedelta(days=30),
            created_by=self.request.user,
            
            # FIXME: Возможно необходима автоматическая генерация содержимого в определенном формате
            # FIXME: Возможно нужно автоматически создавать содержимое поля json
            note=f"""
            Пользователь {self.request.user} #{self.request.user.pk} отправил заявку на становление партнером сервиса:\n
            - Имя: {instance.legal_name}\n
            - ИНН: {instance.inn}\n
            - Юридический адрес: {instance.address}\n
            <a href="{instance.get_admin_url()}">Полная информация</a>\n
            \n
            Проверьте всю информацию и для активации партнера измените статус заявки на ACCEPTED.
            Это будет означать, что договорные отношения между сервисом и партнером, вступают в силу.
            """
        )

        # Сохраняем новые изменения
        instance.save()

        # Создание тикета на утверждение прав пользователя
        # FIXME: Возможно нужно автоматически создавать содержимое поля json
        Ticket.objects.create(
            title=f"Запрос прав на становление Партнером '{instance.legal_name}'",
            ticket_list=TicketList.objects.get(pk=2101),# METASERVICE-ADMIN: Активация партнеров (NEG_REQUEST)
            ticket_type=4, # NEG_REQUEST
            due_date=datetime.now().date() + timedelta(days=30),
            created_by=self.request.user,
            
            # FIXME: Возможно необходима автоматическая генерация содержимого в определенном формате
            note=f"""
            Пользователь {self.request.user} #{self.request.user.pk} отправил заявку на права партнера сервиса.\n
            \n
            <a href="{instance.get_admin_url()}">Полная информация о компании партнера</a>\n
            \n
            После принятия изменений указанное лицо будет партнером сервиса при совершении юридически значимых действий.
            """
        )

        return super().form_valid(form) # Возвращаем успешный ответ

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Сотрудничество",
            "current_page": "cooperate"
        }) 
        return context
    