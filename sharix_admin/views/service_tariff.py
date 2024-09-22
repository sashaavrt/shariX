from django_tables2 import SingleTableView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import UpdateView, CreateView
from sharix_admin.tables import ServiceTariffTable
from sharix_admin.forms import ServiceTariffCreateForm, ServiceTariffUpdateForm
from dbsynce.models import Service
from django.urls import reverse
from django.utils.translation import gettext as _

class ServiceTariffCreate(UserPassesTestMixin, CreateView):
    model = Service
    form_class = ServiceTariffCreateForm
    template_name = "sharix_admin/service_tariff_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': _('Service rates'),
            'object': self.object,
        })
        return context
    
    def get_success_url(self):
        return reverse('service_tariff')
    
    def test_func(self) -> bool or None:
        group_names = ('PARTNER-ADMIN')
        if bool(self.request.user.groups.filter(name=group_names)) or self.request.user.is_superuser:
            return True
        return False

class ServiceTariffListView(UserPassesTestMixin, SingleTableView):
    table_class = ServiceTariffTable
    queryset = Service.objects.all()
    template_name = 'sharix_admin/service_tariff.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': _('Performers'),
            'object_list': context['object_list'],
        }))
        return context
    
    def test_func(self) -> bool or None:
        group_names = ('PARTNER-ADMIN')
        if bool(self.request.user.groups.filter(name=group_names)) or self.request.user.is_superuser:
            return True
        return False


class ServiceTariffUpdateView(UserPassesTestMixin, UpdateView):
    model = Service
    form_class = ServiceTariffUpdateForm
    template_name = "sharix_admin/service_tariff_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': _('Service rates'),
            'object': self.object,
        }))
        return context
    
    def get_success_url(self):
        return reverse('service_tariff')
    
    def test_func(self) -> bool or None:
        group_names = ('PARTNER-ADMIN')
        if bool(self.request.user.groups.filter(name=group_names)) or self.request.user.is_superuser:
            return True
        return False

