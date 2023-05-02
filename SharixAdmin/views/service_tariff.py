from django_tables2 import SingleTableView
from django.views.generic.edit import UpdateView, CreateView
from SharixAdmin.tables import ServiceTariffTable
from SharixAdmin.forms import ServiceTariffCreateForm, ServiceTariffUpdateForm
from metaservicesynced.models import Service
from django.urls import reverse
from SharixAdmin.views.context import get_context

class ServiceTariffCreate(CreateView):
    model = Service
    form_class = ServiceTariffCreateForm
    template_name = "SharixAdmin/service_tariff_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': 'Тарифы услуг',
            'object': self.object,
        }))
        return context
    
    def get_success_url(self):
        return reverse('service_tariff')


class ServiceTariffListView(SingleTableView):
    table_class = ServiceTariffTable
    queryset = Service.objects.all()
    template_name = 'SharixAdmin/service_tariff.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': 'Исполнители',
            'object_list': context['object_list'],
        }))
        return context


class ServiceTariffUpdateView(UpdateView):
    model = Service
    form_class = ServiceTariffUpdateForm
    template_name = "SharixAdmin/service_tariff_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': 'Тарифы услуг',
            'object': self.object,
        }))
        return context
    
    def get_success_url(self):
        return reverse('service_tariff')

