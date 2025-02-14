from datetime import datetime, timedelta
from dbsynce.lib.core import parse_requirements, get_admin_url
from dbsynce.models import Documents
from django.contrib import messages
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from tickets.models import Ticket, TicketList

from sharix_admin.forms import CompanyForm
from sharix_admin.utils import create_ticket_partner_activation
from .base import BaseView


class CooperateView(BaseView, FormView):
    form_class = CompanyForm
    template_name = "sharix_admin/cooperate.html"
    success_url = reverse_lazy("sharix_admin:main")
    page_title = 'Сотрудничество'
    page_name = 'cooperate'

    # Проверяем не состояит ли текущий пользователь в группе PARTNER-ADMIN
    def test_func(self):
        return not "PARTNER-ADMIN" in self.user_groups

    def form_valid(self, form):
        with transaction.atomic():
            # Сохраняем форму, чтобы получить объект компании
            instance = form.save(commit=False)

            # Присваиваем полю repr идентификатор текущего пользователя
            instance.repr = self.request.user

            # Создаем новую запись в БД, чтобы иметь доступ к ID
            instance.save()

            # Создание тикета на активацию партнера.
            # Создаем объект тикета и присваиваем его полю ticket_status
            instance.ticket_status = create_ticket_partner_activation(self.request.user, instance)

            # Создание тикета на утверждение прав пользователя
            Ticket.objects.create(
                title=f"Запрос прав на становление Партнером '{instance.legal_name}'",
                ticket_list=TicketList.objects.get(pk=2102),  # METASERVICE-ADMIN: Права в сервисе (ACCESS_REQUEST)
                ticket_type=3,  # ACCESS_REQUEST
                due_date=datetime.now().date() + timedelta(days=30),
                created_by=self.request.user,

                # FIXME: Возможно нужно автоматически создавать содержимое поля json
                note=f"""
                    Пользователь {self.request.user} #{self.request.user.pk} отправил заявку на права партнера сервиса.\n
                    \n
                    <a href="{get_admin_url(instance)}">Полная информация о компании партнера</a>\n
                    \n
                    После принятия изменений указанное лицо будет партнером сервиса при совершении юридически значимых действий.
                """
            )

            # Сохраняем новые изменения
            instance.save()

            # Создаем необходимые объекты документов по requirements указанных в созданной company
            # Используем bulk_create для создания всех объектов одновременно
            doc_codes = parse_requirements(instance.requirements)
            Documents.objects.bulk_create([
                Documents(
                    company=instance,
                    user=self.request.user,
                    doc_type=doc_code
                ) for doc_code in doc_codes
            ])

        # Отправляем пользователю уведомление на страницу о успехе операции
        messages.success(
            self.request,
            'Ваша заявка на становление партнером успешно отправлена и теперь проходит проверку!'
        )

        return super().form_valid(form)  # Возвращаем успешный ответ
