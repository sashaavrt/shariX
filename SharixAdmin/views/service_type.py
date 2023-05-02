from django_tables2 import SingleTableView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from SharixAdmin.tables import ServiceTypeTable
from SharixAdmin.forms import ServiceTypeCreateForm, ServiceTypeUpdateForm
from metaservicesynced.models import ServiceType
from django.urls import reverse
from SharixAdmin.views.context import get_context

class ServiceTypeCreate(CreateView):
    model = ServiceType
    form_class = ServiceTypeCreateForm
    template_name = "SharixAdmin/service_type_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': 'Услуги сервиса',
            'object': self.object,
        }))
        return context
    
    def get_success_url(self):
        return reverse('service_type')
    

class ServiceTypeListView(SingleTableView):
    table_class = ServiceTypeTable
    queryset = ServiceType.objects.all()
    template_name = 'SharixAdmin/service_type.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': 'Услуги сервиса',
            'object_list': context['object_list'],
        }))
        return context


class ServiceTypeUpdateView(UpdateView):
    model = ServiceType
    form_class = ServiceTypeUpdateForm
    template_name = "SharixAdmin/service_type_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': 'Тарифы услуг',
            'object_list': context['object_list'],
        }))
        return context
    

class ServiceTypeDelete(DeleteView):
    model = ServiceType
    template_name = "SharixAdmin/service_type_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': 'Услуги сервиса',
            'object': self.object,
        }))
        return context
    
    def get_success_url(self):
        return reverse('service_type')