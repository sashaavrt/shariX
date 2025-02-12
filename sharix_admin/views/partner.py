from dbsynce.models import Company, Documents, DocumentFile
from django.contrib import messages
from django.core.files.storage import default_storage
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import FormView

from sharix_admin.forms import CompanyForm, DocumentUploadForm
from sharix_admin.utils import *
from .base import BaseView


class PartnerBaseView(BaseView):
    page_name = 'partner'

    # Проверяем состояит ли текущий пользователь в группе PARTNER-ADMIN
    def test_func(self):
        return "PARTNER-ADMIN" in self.user_groups


class PartnerDetailView(PartnerBaseView, DetailView):
    model = Company
    template_name = 'sharix_admin/partner.html'
    context_object_name = 'company'
    page_title = 'О партнере'

    def get_object(self, queryset=None):
        return get_object_or_404(Company, repr=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        docs = Documents.objects.filter(
            user_id=self.request.user,
            company_id=self.object
        ).prefetch_related('files').order_by('doc_type')

        context.update({"docs": docs})

        return context


class PartnerEditView(PartnerBaseView, FormView):
    template_name = 'sharix_admin/partner_edit.html'
    form_class = CompanyForm
    success_url = reverse_lazy('partner_detail')
    page_title = 'Изменение данных партнера'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = get_object_or_404(Company, repr=self.request.user)
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


class PartnerDocUploadView(PartnerBaseView, FormView):
    # FIXME: Загрузка новых документов должна деактивировать текущего партнера (предварительно это работа обработчиков)
    template_name = 'sharix_admin/partner/doc_upload.html'
    form_class = DocumentUploadForm
    success_url = reverse_lazy('partner_detail')

    def dispatch(self, request, *args, **kwargs):
        self.company = get_object_or_404(Company, repr=self.request.user)
        self.doc = Documents.objects.filter(
            user_id=self.request.user,
            company_id=self.company,
            doc_type=kwargs.get('doc_code')
        ).first()

        self.doc_name = self.doc.get_doc_type_display()
        self.page_title = "Изменение документа партнера: " + self.doc_name

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        with transaction.atomic():
            # Удаляем существующие файлы и записи из базы данных
            existing_files = DocumentFile.objects.filter(document=self.doc)
            for existing_file in existing_files:
                # Удаляем файл с сервера
                if default_storage.exists(existing_file.file.path):
                    default_storage.delete(existing_file.file.path)

                # Удаляем запись о файле из базы данных
                existing_file.delete()

            # Загрузка новых файлов
            doc_file = self.request.FILES.getlist("doc_file")
            for file in doc_file:
                DocumentFile.objects.create(
                    document=self.doc,
                    file=file
                )

            # Создание нового тикета и архивация старого
            if self.doc.ticket_status:
                self.doc.ticket_status.archive()

            self.doc.expire_date = self.request.POST.get('doc_expire_date') if self.request.POST[
                'doc_expire_date'] else None
            self.doc.ticket_status = create_ticket_partner_docs_verification(self.request.user, self.company, self.doc)

            self.doc.save()

        # Отправляем пользователю уведомление на страницу об успехе операции
        messages.success(self.request,
                         f'Файлы документа "{self.doc_name}" успешно загружены и теперь проходят проверку!')
        return super().form_valid(form)


class PartnerDocView(PartnerBaseView, DetailView):
    model = Documents
    template_name = 'sharix_admin/partner/doc.html'
    context_object_name = 'doc'

    def dispatch(self, request, *args, **kwargs):
        self.company = get_object_or_404(Company, repr=self.request.user)

        self.doc = Documents.objects.filter(
            user_id=self.request.user,
            company_id=self.company,
            doc_type=kwargs.get('doc_code')
        ).first()

        if not self.doc:
            return self.handle_no_permission()

        self.doc_name = self.doc.get_doc_type_display()
        self.page_title = _("Детали документа: ") + self.doc_name

        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.doc

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doc_files = DocumentFile.objects.filter(document=self.doc)
        context.update({"doc_files": doc_files})
        return context
