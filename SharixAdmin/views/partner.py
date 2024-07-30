from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.db import transaction

from dbsynce.models import Company, Documents
from SharixAdmin.forms import CompanyForm, DocumentUploadForm
from SharixAdmin.utils import *

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

        docs = Documents.objects.filter(
            user_id=self.request.user,
            company_id=self.object
        ).prefetch_related('files').order_by('doc_type')

        context.update({ "docs": docs }) 

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

        # Отправляем полAьзователю уведомление на страницу об успехе операции
        messages.success(self.request, 'Данные успешно изменены и теперь проходят проверку!')
        return super().form_valid(form)


class PartnerDocEditView(PartnerBaseView, FormView):       
    template_name = 'SharixAdmin/partner_doc.html'
    form_class = DocumentUploadForm
    success_url = reverse_lazy('partner_detail')

    def dispatch(self, request, *args, **kwargs):
        self.doc_code = kwargs.get("doc_code")
        self.doc_name = Documents.DOC_TYPES_DICT[self.doc_code]
        self.page_title = _("Изменение документа партнера: ") + self.doc_name
        self.company = get_object_or_404(Company, repr_id=self.request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        with transaction.atomic():
            doc_file = self.request.FILES.getlist("doc_file")
            
            for file in doc_file:
                print(file)

            create_ticket_partner_docs_verification(self.request.user, self.company, self.doc_name, self.doc_code)

        # Отправляем полAьзователю уведомление на страницу об успехе операции
        messages.success(self.request, f'Файлы документа "{self.doc_name}" успешно загружены и теперь проходят проверку!')
        return super().form_valid(form)