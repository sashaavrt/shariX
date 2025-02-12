from dbsynce.models import ServiceType
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django_tables2 import SingleTableView

from sharix_admin.forms import ServiceTypeCreateForm, ServiceTypeUpdateForm
from sharix_admin.tables import ServiceTypeTable
from .base import BaseView


class ServiceTypeCreate(BaseView, CreateView):
    page_title = _('Услуги сервиса')
    page_name = 'service_type'
    model = ServiceType
    form_class = ServiceTypeCreateForm
    template_name = "sharix_admin/service_type_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'object': self.object,
        })
        return context

    def get_success_url(self):
        return reverse('service_type')

    def test_func(self) -> bool or None:
        group_names = ('METASERVICE-ADMIN')
        if bool(self.request.user.groups.filter(name=group_names)) or self.request.user.is_superuser:
            return True
        return False


class ServiceTypeListView(BaseView, SingleTableView):
    page_title = _('Услуги сервиса')
    page_name = 'service_type'
    table_class = ServiceTypeTable
    queryset = ServiceType.objects.all()
    template_name = 'sharix_admin/service_type.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'object_list': context['object_list'],
        })
        return context

    def testing(self, queryset, is_descending):
        queryset = queryset.annotate.order_by("-" if is_descending else "")
        return (queryset, True)

    def test_func(self) -> bool or None:
        group_names = ('METASERVICE-ADMIN')
        if bool(self.request.user.groups.filter(name=group_names)) or self.request.user.is_superuser:
            return True
        return False


class ServiceTypeUpdateView(BaseView, UpdateView):
    model = ServiceType
    form_class = ServiceTypeCreateForm
    template_name = "sharix_admin/service_type_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': _('Услуги сервиса'),
            'object': self.object,
            "current_page": "service_type"
        })
        return context

    def test_func(self) -> bool or None:
        group_names = ('METASERVICE-ADMIN')
        if bool(self.request.user.groups.filter(name=group_names)) or self.request.user.is_superuser:
            return True
        return False

    def get_success_url(self):
        return reverse('service_type')


class ServiceTypeDelete(BaseView, DeleteView):
    model = ServiceType
    template_name = "sharix_admin/service_type_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Услуги сервиса',
            'object': self.object,
            "current_page": "service_type"
        })
        return context

    def get_success_url(self):
        return reverse('service_type')

    def test_func(self) -> bool or None:
        group_names = ('METASERVICE-ADMIN')
        if bool(self.request.user.groups.filter(name=group_names)) or self.request.user.is_superuser:
            return True
        return False
