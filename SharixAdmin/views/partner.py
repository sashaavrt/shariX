from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.db import transaction

from dbsynce.models import Company, Documents
from SharixAdmin.forms import CompanyForm
from SharixAdmin.utils import create_ticket_partner_activation

from .base import BaseView


class PartnerDetailView(UserPassesTestMixin, BaseView, DetailView):
    model = Company
    template_name = 'SharixAdmin/partner.html'
    context_object_name = 'company'

    page_title = _('О партнере')
    page_name = 'partner'

    # Проверяем состояит ли текущий пользователь в группе PARTNER-ADMIN
    def test_func(self):
        return self.request.user.groups.filter(name='PARTNER-ADMIN').exists()

    def get_object(self, queryset=None):
        return get_object_or_404(Company, repr_id=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "company_documents": Documents.parse_requirements(self.object.requirements)
        }) 
        return context
    


class PartnerEditView(UserPassesTestMixin, BaseView, FormView):
    template_name = 'SharixAdmin/partner_edit.html'
    form_class = CompanyForm
    success_url = reverse_lazy('partner_detail')

    page_title = _('Изменение данных партнера')
    page_name = 'partner'

    # Проверяем состояит ли текущий пользователь в группе PARTNER-ADMIN
    def test_func(self):
        return self.request.user.groups.filter(name='PARTNER-ADMIN').exists()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = get_object_or_404(Company, repr_id=self.request.user)
        return kwargs

    def form_valid(self, form):
        with transaction.atomic():
            # Сохраняем изменения
            form.save()

            # Получаем текущий объект компании и деактивируем ее
            current_company = form.instance
            current_company.deactivate()

            # Выполняем пересоздание тикета на активацию партнера
            current_company.ticket_status.archive()
            create_ticket_partner_activation(self.request.user, current_company)

        # Отправляем пользователю уведомление на страницу о успехе операции
        messages.success(self.request, 'Данные успешно изменены и теперь проходят проверку!')
        return super().form_valid(form)