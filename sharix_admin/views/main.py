from django.views.generic import TemplateView
from django.utils.translation import gettext as _

from .base import BaseView


class MainView(BaseView, TemplateView):
    page_title = 'Добро пожаловать!'
    page_name = 'main'
    template_name = 'sharix_admin/main.html'