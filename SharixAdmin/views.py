
import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, resolve, reverse
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.contrib.auth import logout
from django.db.models import Q
from .tables import *
from django import template
# Create your views here.


@login_required
def index(request):

    ph_num = str(request.user.phone_number)
    convert_ph_num = f"+{ph_num[:1]} ({ph_num[1:4]}) {ph_num[4:7]}-{ph_num[7:9]}-{ph_num[9:11]}"
    #print(convert_ph_num)
    context = get_context(request, {
        'title':'Главная/баланс',
        'phone':convert_ph_num
    })
    
    return render(request, 'SharixAdmin/main.html', context)

@login_required
def transactions(request):
    
    context = get_context(request, {
        'title':'История платежей',
        })
        
    return render(request, 'SharixAdmin/transactions.html', context)

@login_required
def trans_id(request, trans_id):
    
    
    
    context = get_context(request, {
        'title':'Услуга'
        })
    return render(request, 'SharixAdmin/trans_carried.html', context)

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


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('authweb'))

class LoginSharix(LoginView):
    form_class = LoginUserForm
    template_name = 'SharixAdmin/auth.html'

    
    def get_success_url(self):
        return reverse_lazy('home')

def testPage(request):
    context = get_context(request, {
        'title':'Страница в разработке'
        })
    return render(request, "SharixAdmin/test.html", context)




menu = [
    {'title':'Главная/баланс',          'link':'home', 'sel':'house'},
    {'title':'Платежная информация',    'link':'test-page', 'sel':'credit-card'},
    {'title':'История платежей',        'link':'trans','sel':'clock-history'},
    {'title':'Курсы',                   'link':'course', 'sel':'education'},
    {'title':'Личная информация',       'link':'test-page', 'sel':'person'},
    {'title':'Управление сервисами',    'link':'test-page', 'sel':'hdd-network'},
    {'title':'Мои связи',               'link':'test-page', 'sel':'people'},
    {'title':'Сотрудничество',          'link':'test-page', 'sel':'sotrud'},
    {'title':'Техподдержка',            'link':'test-page', 'sel':'gear'},
    {'title':'Мои заявки',              'link':'todo', 'sel':'tikets'},
]

def get_context(request, page_context) -> dict:
    base_context = {
        "title":page_context['title'],
        'url_path':resolve(request.path_info).url_name,
        'menu':menu
    }
    context = dict(list(base_context.items()) + list(page_context.items()))
    return context




#Shema views
@login_required
def schema_v3(request):
    
    return render(request, "SharixAdmin/schema.html")





    



