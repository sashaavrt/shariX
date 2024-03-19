from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _


@login_required
def trans_id(request, trans_id):
    context = {
        'title':_('Service')
    }
    return render(request, 'SharixAdmin/trans_carried.html', context)