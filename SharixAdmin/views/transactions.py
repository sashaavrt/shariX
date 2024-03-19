from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.translation import gettext as _

@login_required
def transactions(request):
    
    context = {
        'title':_('Payment history'),
        'current_page': 'transactions'
    }
        
    return render(request, 'SharixAdmin/transactions.html', context)