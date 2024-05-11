from django.views.generic import TemplateView
from django.utils.translation import gettext as _

from .base import BaseView


class IndexView(BaseView, TemplateView):
    page_title = _('Home/Balance')
    page_name = 'index'
    template_name = 'SharixAdmin/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ph_num = str(self.request.user.phone_number)
        convert_ph_num = f"+{ph_num[:1]} ({ph_num[1:4]}) {ph_num[4:7]}-{ph_num[7:9]}-{ph_num[9:11]}"

        context.update({
            'phone': convert_ph_num,
        })

        return context