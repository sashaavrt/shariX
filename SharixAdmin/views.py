
import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, resolve, reverse
from django.contrib.auth.decorators import login_required
from django_tables2 import SingleTableView
from .forms import *
from SharixAdmin.models import *
from django.contrib.auth import logout
from django.db.models import Q
from .tables import *
from django import template
from django.views.generic.edit import UpdateView, CreateView
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
        print(self.request.GET['next'])
        
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
    {'title':'Мои заявки',              'link':'tickets', 'sel':'tikets'},
    {'title':'Исполнители',             'link':'provider', 'sel':'people'},
    {'title':'Тарифы услуг',            'link':'service_tariff', 'sel':'person'},
]

def get_context(request, page_context) -> dict:
    base_context = {
        "title":page_context['title'],
        'url_path':resolve(request.path_info).url_name,
        'menu':menu
    }
    context = dict(list(base_context.items()) + list(page_context.items()))
    return context


@login_required
def change_provider_status(request):
    if request.method == 'POST':
        provider_id = request.POST.get('provider_id')
        new_status = request.POST.get('new_status')
        
        provider = Provider.objects.get(pk=provider_id)
        provider.status = new_status
        provider.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})

class ServiceTariffUpdateView(UpdateView):
    model = Service
    form_class = ServiceTariffUpdateForm
    template_name = "SharixAdmin/service_tariff_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': 'Тарифы услуг',
            'object': self.object,
        }))
        return context
    
    def get_success_url(self):
        return reverse('service_tariff')

class ServiceTariffCreate(CreateView):
    model = Service
    form_class = ServiceTariffCreateForm
    template_name = "SharixAdmin/service_tariff_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': 'Тарифы услуг',
            'object': self.object,
        }))
        return context
    
    def get_success_url(self):
        return reverse('service_tariff')

class ProviderListView(SingleTableView):
    table_class = ProviderTable
    queryset = Provider.objects.all()
    template_name = 'SharixAdmin/provider.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': 'Исполнители',
            'object_list': context['object_list'],
        }))
        return context

class ServiceTariffListView(SingleTableView):
    table_class = ServiceTariffTable
    queryset = Service.objects.all()
    template_name = 'SharixAdmin/service_tariff.html'
    # paginate_by = 2


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': 'Тарифы услуг',
            'object_list': context['object_list'],
        }))
        return context

#Shema views
@login_required
def schema_v3(request):
    
    return render(request, "SharixAdmin/schema.html")





    



