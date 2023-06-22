from django.shortcuts import render
from SharixAdmin.forms import PartnerInformationCreateForm, PartnerInformationUpdateForm
from SharixAdmin.groups import group_required
from metaservicesynced.models import Company
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import UpdateView, CreateView
from SharixAdmin.views.context import get_context
from django.urls import reverse
from django.utils.translation import gettext as _

from core.utils.AuthAPI import AuthAPI
from tickets.models import Task
from core.config import API_URL
api = AuthAPI("89855703300", "12345")
import requests
from django.urls import reverse_lazy
from django.contrib.auth.hashers import check_password

import xmpp
from xmpp import cli

class PartnerInformationCreate(UserPassesTestMixin, CreateView):
    model = Company
    form_class = PartnerInformationCreateForm
    template_name = "SharixAdmin/partner_information_form.html"
    success_url = reverse_lazy("SharixAdmin:partners")

    def form_valid(self, form):
        form.instance.representative_id = self.request.user
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
        cli.send_message("open_tickets_backend@ej.sharix-app.org", "eb177b1c9f99a7a13798928318d7a72c", "open_strequest_new@ej.sharix-app.org", str(jso))
        return responce

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': _('Partner Information'),
            'object': self.object,
        }))
        return context
    
    def get_success_url(self):
        return reverse('partners')
    
    def test_func(self) -> bool or None:
        group_names = ('PARTNER-ADMIN')
        if bool(self.request.user.groups.filter(name=group_names)) or self.request.user.is_superuser:
            return True
        return False
    
class PartnerInformationUpdateView(UserPassesTestMixin, UpdateView):
    model = Company
    form_class = PartnerInformationUpdateForm
    template_name = "SharixAdmin/partner_information_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': _('Partner Information'),
            'object': self.object,
        }))
        return context
    
    def get_success_url(self):
        return reverse('test-page')
    
    def test_func(self) -> bool or None:
        group_names = ('PARTNER-ADMIN')
        if bool(self.request.user.groups.filter(name=group_names)) or self.request.user.is_superuser:
            return True
        return False


def partner_information(request):
    context = get_context(request, {
        'title':_('Partner Information'),
        })
    
    return render(request, 'SharixAdmin/partner_information.html', context)