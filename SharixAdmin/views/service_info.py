from SharixAdmin.forms import ServiceInformationCreateForm, ServiceInformationUpdateForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView
from metaservicesynced.models import Service
from SharixAdmin.views.context import get_context
from django.urls import reverse
from django.utils.translation import gettext as _

from core.utils.AuthAPI import AuthAPI
from tickets.models import Task
from core.config import API_URL
api = AuthAPI("89855703300", "12345")
import requests
from django.urls import reverse_lazy
from datetime import timezone

class ServiceInformationCreate(UserPassesTestMixin, CreateView):
    model = Service
    form_class = ServiceInformationCreateForm
    template_name = "SharixAdmin/service_information_form.html"
    success_url = reverse_lazy("SharixAdmin:service_tariff")

    def form_valid(self, form):
        new_ticket = {
            "task_list": 1,
            "created_by": self.request.user.pk,
            "type": 1,
            "title": "service_create",
            "note": str(form.data),
        }
        resp = requests.post(f"{API_URL}/tickets/api/tickets/", data=new_ticket, headers=api.headers)
        jso = resp.json()
        form.instance.ticket_status = Task.objects.get(pk=int(jso['id']))
        print(form.cleaned_data)
        responce = super().form_valid(form)
        return responce


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': _('Information about the service'),
            'object': self.object,
            
        }))
        return context
    
    def get_success_url(self):
        return reverse('service_tariff')
    
    
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
            'title': 'Information about the service',
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