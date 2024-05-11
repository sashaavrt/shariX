from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.translation import gettext as _


@login_required
def index(request):
    ph_num = str(request.user.phone_number)
    convert_ph_num = f"+{ph_num[:1]} ({ph_num[1:4]}) {ph_num[4:7]}-{ph_num[7:9]}-{ph_num[9:11]}"

    context = {
        'title':_('Home/Balance'),
        'phone':convert_ph_num,
        'current_page': 'index',
        "is_partner_admin": request.user.groups.filter(name='PARTNER-ADMIN').exists()
    }
    
    return render(request, 'SharixAdmin/main.html', context)