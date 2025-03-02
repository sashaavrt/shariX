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


class ServiceListView(UserPassesTestMixin, SingleTableView):
    table_class = ServiceTable
    queryset = Service.objects.all()
    template_name = 'sharix_admin/service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': _('Услуги сервиса'),
            'object_list': context['object_list']
        })
        return context

    def test_func(self) -> bool or None: # type: ignore
        group_names = ('PROVIDER')
        if bool(self.request.user.groups.filter(name=group_names)) or self.request.user.is_superuser:
            return True
        return False


@login_required
@group_required('PROVIDER')
def change_service_status(request):
    if request.method == 'POST':
        service_id = request.POST.get('service_id')
        new_status = request.POST.get('new_status')

        service = Service.objects.get(pk=service_id)
        service.status = new_status
        service.save()

def change_status():
    return None
