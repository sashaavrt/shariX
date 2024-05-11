from django.views.generic import TemplateView
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import UserPassesTestMixin

from .base import BaseView


class PartnerView(UserPassesTestMixin, BaseView, TemplateView):
    page_title = _('О партнере')
    page_name = 'partner'
    template_name = 'SharixAdmin/partner.html'

    # Проверяем состояит ли текущий пользователь в группе PARTNER-ADMIN
    def test_func(self):
        return self.request.user.groups.filter(name='PARTNER-ADMIN').exists()