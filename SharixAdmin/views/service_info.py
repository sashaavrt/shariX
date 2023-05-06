from SharixAdmin.forms import ServiceInformationCreateForm, ServiceInformationUpdateForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView
from metaservicesynced.models import Service
from SharixAdmin.views.context import get_context
from django.urls import reverse

class ServiceInformationCreate(UserPassesTestMixin, CreateView):
    model = Service
    form_class = ServiceInformationCreateForm
    template_name = "SharixAdmin/service_information_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': 'Информация о сервисе',
            'object': self.object,
            
        }))
        return context
    
    def get_success_url(self):
        return reverse('test-page')
    
    def test_func(self) -> bool or None:
        group_names = ('METASERVICE-ADMIN')
        if bool(self.request.user.groups.filter(name=group_names)) or self.request.user.is_superuser:
            return True
        return False
    
class ServiceInformationUpdateView(UserPassesTestMixin, UpdateView):
    model = Service
    form_class = ServiceInformationUpdateForm
    template_name = "SharixAdmin/service_information_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': 'Информация о сервисе',
            'object': self.object,
        }))
        return context
    
    def get_success_url(self):
        return reverse('test-page')
    
    def test_func(self) -> bool or None:
        group_names = ('METASERVICE-ADMIN')
        if bool(self.request.user.groups.filter(name=group_names)) or self.request.user.is_superuser:
            return True
        return False