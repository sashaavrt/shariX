from django.contrib.auth.decorators import login_required
from SharixAdmin.views.context import get_context
from django.shortcuts import render

@login_required
def transactions(request):
    
    context = get_context(request, {
        'title':'История платежей',
        })
        
    return render(request, 'SharixAdmin/transactions.html', context)