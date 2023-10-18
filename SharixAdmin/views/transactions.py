from django.contrib.auth.decorators import login_required
from SharixAdmin.views.context import get_context
from django.shortcuts import render
from django.utils.translation import gettext as _

@login_required
def transactions(request):
    
    context = get_context(request, {
        'title':_('Payment history'),
        })
        
    return render(request, 'SharixAdmin/transactions.html', context)