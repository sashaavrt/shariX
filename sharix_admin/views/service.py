from dbsynce.models import Service, ServiceType
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils.translation import gettext as _
from django_tables2 import SingleTableView
from django.contrib import messages
from django.db import transaction
from sharix_admin.tables import ServiceTable
from sharix_admin.utils import group_required
from django.http import HttpResponse
from django.shortcuts import render
from .base import BaseView
from django.views.generic.edit import FormView
from sharix_admin.forms import *
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView

class ServiceBaseView(BaseView):
    page_name = 'service'


class ServiceDetailView(ServiceBaseView, DetailView):
    model = Service
    template_name = 'sharix_admin/service_about.html'
    context_object_name = 'service'
    page_title = 'Об услуге'

    def get_object(self, queryset=None):
        return get_object_or_404(Service, id=Service.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ServiceEditView(ServiceBaseView, FormView):
    template_name = 'sharix_admin/service_edit.html'
    form_class = ServiceInformationUpdateForm
    success_url = reverse_lazy('partner_detail')
    page_title = 'Изменение данных услуги'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = get_object_or_404(Service, repr=self.request.user)
        return kwargs

    def form_valid(self, form):
        with transaction.atomic():
            form.save()
        messages.success(self.request, 'Данные успешно изменены и теперь проходят проверку!')
        return super().form_valid(form)