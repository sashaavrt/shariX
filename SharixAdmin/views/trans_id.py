from django.shortcuts import render
from SharixAdmin.views.context import get_context
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _

@login_required
def trans_id(request, trans_id):
    context = get_context(request, {
        'title':_('Service')
        })
    return render(request, 'SharixAdmin/trans_carried.html', context)