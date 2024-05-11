from django.views.generic import TemplateView
from django.utils.translation import gettext as _

from .base import BaseView


class TransactionsView(BaseView, TemplateView):
    page_title = _('Payment history')
    page_name = 'transactions'
    template_name = 'SharixAdmin/transactions.html'