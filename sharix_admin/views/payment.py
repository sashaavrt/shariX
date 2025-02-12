from django.utils.translation import gettext as _
from django.views.generic import TemplateView

from .base import BaseView


class PaymentView(BaseView, TemplateView):
    page_title = _('Оплата')
    page_name = 'payment'
    template_name = 'sharix_admin/payment.html'
