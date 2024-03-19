from django_tables2 import SingleTableView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from SharixAdmin.tables import ServiceTypeTable
from django.contrib.auth.mixins import UserPassesTestMixin
from SharixAdmin.forms import ServiceTypeCreateForm, ServiceTypeUpdateForm
from dbsynce.models import ServiceType
from django.urls import reverse
from django.utils.translation import gettext as _

    
    
class ServiceTypeCreate(UserPassesTestMixin, CreateView):
    model = ServiceType
    form_class = ServiceTypeCreateForm
    template_name = "SharixAdmin/service_type_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': _('Услуги сервиса'),
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
    
    
    

    

class ServiceTypeListView(UserPassesTestMixin, SingleTableView):
    table_class = ServiceTypeTable
    queryset = ServiceType.objects.all()
    template_name = 'SharixAdmin/service_type.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Услуги сервиса',
            'object_list': context['object_list'],
            "current_page": "service_type"
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

class ServiceTypeUpdateView(UserPassesTestMixin, UpdateView):
    model = ServiceType
    form_class = ServiceTypeCreateForm
    template_name = "SharixAdmin/service_type_form.html"

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
    

class ServiceTypeDelete(UserPassesTestMixin, DeleteView):
    model = ServiceType
    template_name = "SharixAdmin/service_type_delete.html"

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
    
