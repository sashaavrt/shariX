from django.contrib.auth.decorators import login_required
from SharixAdmin.views.context import get_context
from django.shortcuts import render
from django.utils.translation import gettext as _


@login_required
def index(request):

    ph_num = str(request.user.phone_number)
    convert_ph_num = f"+{ph_num[:1]} ({ph_num[1:4]}) {ph_num[4:7]}-{ph_num[7:9]}-{ph_num[9:11]}"
    #print(convert_ph_num)
    context = get_context(request, {
        'title':_('Home/Balance'),
        'phone':convert_ph_num
    })
    
    return render(request, 'SharixAdmin/main.html', context)