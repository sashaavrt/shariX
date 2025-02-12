from django.utils.translation import gettext as _
from django.views.generic import TemplateView

from .base import BaseView


class TransactionsView(BaseView, TemplateView):
    page_title = _('Payment history')
    page_name = 'transactions'
    template_name = 'sharix_admin/transactions.html'
