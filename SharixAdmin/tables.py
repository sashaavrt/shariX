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
        

class ServiceTypeTable(tables.Table):

    id = tables.Column(verbose_name='ID', attrs={"td":{"width":"5%"}})
    caption = tables.LinkColumn('service_type/edit/', verbose_name='Название услуги', text = lambda record: record.caption,
        args=[tables.A('pk')], attrs={'th':{'scope':'col'}, "td":{"width":"100%"},})
    deletee = tables.LinkColumn('service_type/delete/', verbose_name='', text = "Удалить",
        args=[tables.A('pk')], attrs={'th':{'scope':'col'}, "td":{"width":"auto"},})
    
    class Meta:
        model = ServiceType
        attrs = {"class": "table table-layout-fixed text-start"}
        exclude = ('codename','description','requirements',
                   'price_type','status','ticket_status', 
                   'id_metaservice', 'link_agreement',
                   'is_global', 'is_visible',)

    def render_delete(self, value, record):
        return format_html('<a href="/service_type/delete" class="btn btn-outline-danger">Удалить</a>')
        