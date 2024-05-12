from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import UserPassesTestMixin

from dbsynce.models import Company
from SharixAdmin.forms import CompanyForm

from .base import BaseView


class PartnerDetailView(UserPassesTestMixin, BaseView, DetailView):
    model = Company
    template_name = 'SharixAdmin/partner.html'
    context_object_name = 'company'

    page_title = _('О партнере')
    page_name = 'partner'

    # Проверяем состояит ли текущий пользователь в группе PARTNER-ADMIN
    def test_func(self):
        return self.request.user.groups.filter(name='PARTNER-ADMIN').exists()

    def get_object(self, queryset=None):
        return get_object_or_404(Company, repr_id=self.request.user)


class PartnerEditView(UserPassesTestMixin, BaseView, FormView):
    template_name = 'SharixAdmin/partner_edit.html'
    form_class = CompanyForm
    success_url = reverse_lazy('partner_detail')

    page_title = _('Изменение данных партнера')
    page_name = 'partner'

    # Проверяем состояит ли текущий пользователь в группе PARTNER-ADMIN
    def test_func(self):
        return self.request.user.groups.filter(name='PARTNER-ADMIN').exists()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = get_object_or_404(Company, repr_id=self.request.user)
        return kwargs

    def form_valid(self, form):
        form.save()  # Сохраняем изменения
        return super().form_valid(form)