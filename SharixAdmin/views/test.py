from SharixAdmin.views.context import get_context
from django.shortcuts import render
from django.utils.translation import gettext as _

def testPage(request):
    context = get_context(request, {
        'title':_('Page in development')
        })
    return render(request, "SharixAdmin/test.html", context)