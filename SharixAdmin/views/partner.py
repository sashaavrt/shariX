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


class PartnerBaseView(UserPassesTestMixin, BaseView):
    page_name = 'partner'

    # Проверяем состояит ли текущий пользователь в группе PARTNER-ADMIN
    def test_func(self):
        return self.request.user.groups.filter(name='PARTNER-ADMIN').exists()


class PartnerDetailView(PartnerBaseView, DetailView):
    model = Company
    template_name = 'SharixAdmin/partner.html'
    context_object_name = 'company'
    page_title = _('О партнере')
    

    def get_object(self, queryset=None):
        return get_object_or_404(Company, repr_id=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            "doc_codes": Documents.parse_requirements(self.object.requirements),
            "doc_dict": Documents.DOC_TYPES_DICT
        }) 

        return context


class PartnerEditView(PartnerBaseView, FormView):
    template_name = 'SharixAdmin/partner_edit.html'
    form_class = CompanyForm
    success_url = reverse_lazy('partner_detail')
    page_title = _('Изменение данных партнера')


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


class PartnerDocDetailView(PartnerBaseView, DetailView):       
    template_name = 'SharixAdmin/partner_doc.html'
    
    def get_object(self, queryset=None):
        doc_code = self.kwargs.get("doc_code")
        self.page_title = _("Изменение документа партнера: ") + Documents.DOC_TYPES_DICT[doc_code]

        doc = Documents.objects.filter().first()
        return doc

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context