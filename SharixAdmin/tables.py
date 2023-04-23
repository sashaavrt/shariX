import django_tables2 as tables

from metaservicesynced.models import *
from .models import *
from django.utils.html import format_html

class TransactionsWalletTable(tables.Table):
    # id = tables.Column(order_by=True)
    id = tables.Column(verbose_name='#', orderable=False,                                       attrs={"td":{"width":"5%"}})
    wallet = tables.Column(verbose_name='Владелец', orderable=False,                            attrs={"td":{"width":"15%"}})
    name_operation = tables.Column(verbose_name='Услуга', attrs={'th':{'scope':'col'},          "td":{"width":"20%"}}) 
    price = tables.Column(verbose_name='Баллы', attrs={"class":"row",                           "td":{"width":"10%"}})
    date_operation = tables.Column(verbose_name='Дата оформления',                              attrs={"td":{"width":"30%"}})
    is_carried_out = tables.BooleanColumn(verbose_name='Статус', orderable=False, yesno="Успешно,Не успешно", attrs={"td":{"width":"20%"}})
    
    class Meta:
        #model = TransactionsWallets
        attrs = {"class": "table table-striped"}
        exclude = ("balance_before", 
                   "amount", 
                   "metaservice_id", 
                   "transaction_type",
                   "doc_num",
                   "service_id")

    def render_name_operation(self, value, record):
        return format_html("<a href='{}'>{}</a>", record.get_absolute_url(), value)
   
class ServiceTable(tables.Table):

    id = tables.Column(verbose_name='ID', attrs={"td":{"width":"5%"}})
    servicetype_id = tables.Column(verbose_name='Название тарифа', accessor = 'servicetype_id.caption',
        attrs={'th':{'scope':'col'}, "td":{"width":"20%"}})
    # servicetype_id = tables.Column(verbose_name='Название тарифа', accessor = 'servicetype_id.description',
    #     attrs={'th':{'scope':'col'}, "td":{"width":"20%"}})
    price_km = tables.Column(verbose_name='Стоимость км.', attrs={'th':{'scope':'col'}, "td":{"width":"20%"}})
    price_min = tables.Column(verbose_name='Стоимость мин.', attrs={'th':{'scope':'col'}, "td":{"width":"20%"}})
    price_amount = tables.Column(verbose_name='Стоимость услуги', attrs={'th':{'scope':'col'}, "td":{"width":"20%"}})
    status = tables.Column(verbose_name='Статус', attrs={'th':{'scope':'col'}, "td":{"width":"20%"}}) 
    check = tables.BooleanColumn(verbose_name='', attrs={'th':{'scope':'col'}, "td":{"width":"20%"}})
    paginate_by = 10
    class Meta:
        model = Service
        attrs = {"class": "table table-layout-fixed"}
        exclude = ('resource_id', 'requirements', 'id_provider',
                   'id_metaservice', 'price_alg', 'service_status', 'ticket_status',
                    'is_global', 'is_visible')

    def render_check(self, value, record):
        if record.status == 'active':
            return format_html('<input class="form-check-input status-toggle" checked type="checkbox" id="flexCheckDefault" data-service-id="{}">', record.id)
        else:
            return format_html('<input class="form-check-input status-toggle" type="checkbox" id="flexCheckDefault" data-service-id="{}">', record.id)     

    