from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from SharixAdmin.views.context import get_context

@login_required
def balance(request):
    context = get_context(request, {
        'title':'Пополнить баланс'
        })
    if request.method == 'POST':
        if float(request.POST['price']) > 0:
            context = get_context(request, {
                'title':'Пополнить баланс',
                'msg':'Оплата прошла успешно ;)'
                })
            return render(request, "SharixAdmin/balance_success.html", context)
        else:
            context = get_context(request, {
                'title':'Пополнить баланс',
                'msg':'Оплата не прошла ;('
                })
            return render(request, "SharixAdmin/balance_success.html", context)

    
    return render(request, "SharixAdmin/balance.html", context)