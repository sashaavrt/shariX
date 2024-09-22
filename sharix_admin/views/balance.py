from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _

@login_required
def balance(request):
    context = get_context(request, {
        'title':_('Top up your balance')
        })
    if request.method == 'POST':
        if float(request.POST['price']) > 0:
            context = get_context(request, {
                'title':_('Top up your balance'),
                'msg':_('The payment was successful ;)')
                })
            return render(request, "sharix_admin/balance_success.html", context)
        else:
            context = get_context(request, {
                'title':_('Top up your balance'),
                'msg':_('Payment failed ;(')
                })
            return render(request, "sharix_admin/balance_success.html", context)

    
    return render(request, "sharix_admin/balance.html", context)