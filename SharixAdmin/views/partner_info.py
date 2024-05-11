from django.shortcuts import render
from SharixAdmin.forms import PartnerInformationCreateForm, PartnerInformationUpdateForm
from SharixAdmin.groups import group_required
from dbsynce.models import Company
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse
from django.utils.translation import gettext as _

from core.utils.AuthAPI import AuthAPI
from tickets.models import Ticket
from core.settings import API_URL
api = AuthAPI("79999999999", "Pa$$w0rd1")
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
        form.instance.ticket_status = Ticket.objects.get(pk=int(jso['id']))
        print(form.cleaned_data)
        responce = super().form_valid(form)
        cli.send_message("open_tickets_backend@ej.sharix-app.org", "eb177b1c9f99a7a13798928318d7a72c", "open_strequest_new@ej.sharix-app.org", str(jso))
        return responce

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': _('Partner Information'),
            'object': self.object,
        })
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
    
    def form_valid(self, form):
        # Получаем текущий объект Company
        self.object = form.save()

        # Проверяем, изменились ли поля inn, ogrn, kpp, ответственный, название
        if (self.object.inn != form.initial['inn'] or
            self.object.ogrn != form.initial['ogrn'] or
            self.object.kpp != form.initial['kpp'] or
            self.object.repr_id != form.initial['repr_id'] or
            self.object.legal_name != form.initial['legal_name']):
            new_ticket = {
            "ticket_list": 1,
            "created_by": self.request.user.pk,
            "type": 1,
            "title": "service_update",
            "note": str(form.data),
            }
            resp = requests.post(f"{API_URL}/tickets/api/tickets/", data=new_ticket, headers=api.headers)
            jso = resp.json()
            form.instance.ticket_status = Ticket.objects.get(pk=int(jso['id']))
            print(form.cleaned_data)
            cli.send_message("open_tickets_backend@ej.sharix-app.org", "eb177b1c9f99a7a13798928318d7a72c", "open_strequest_new@ej.sharix-app.org", str(jso))
            self.object.status = "deactivate"
            responce = super().form_valid(form)
            return responce
        else:
            return super().form_valid(form)

    def get_success_url(self):
        return reverse('test-page')
    
    def test_func(self) -> bool or None:
        group_names = ('PARTNER-ADMIN')
        if bool(self.request.user.groups.filter(name=group_names)) or self.request.user.is_superuser:
            return True
        return False