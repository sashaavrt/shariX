from django.shortcuts import render
from django.utils.translation import gettext as _

def paymentView(request):
    context = {
        'title':_('Оплата'),
        'current_page': 'payment'
    }
    return render(request, "SharixAdmin/test.html", context)
