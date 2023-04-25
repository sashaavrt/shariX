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
        
class PartnersTable(tables.Table):

    id = tables.Column(verbose_name='ID', attrs={"td":{"width":"5%"}})
    legal_name = tables.Column(verbose_name='Юрлицо', attrs={'th':{'scope':'col'}, "td":{"width":"20%"}})
    repr_id = tables.Column(accessor='repr_id.full_name', order_by=('repr_id.first_name', 'repr_id.last_name'), verbose_name='Ответственный', attrs={"td":{"width":"15%"}})
   
    status = tables.Column(verbose_name='Статус', attrs={'th':{'scope':'col'}, "td":{"width":"20%"}}) 
    check = tables.BooleanColumn(verbose_name='', attrs={'th':{'scope':'col'}, "td":{"width":"20%"}})
    # paginate_by = 10
    class Meta:
        model = Company
        attrs = {"class": "table table-layout-fixed"}
        exclude = ('inn','kpp','ogrn', 'bank_name', 
                   'bik', 'ks', 'rs', 
                   'address', 'requirements', 
                   'id_metaservice', 'is_global', 'is_visible', 'ticket_status')

    def render_check(self, value, record):
        if record.status == 'active':
            return format_html('<input class="form-check-input status-toggle" checked type="checkbox" id="flexCheckDefault" data-partners-id="{}">', record.id)
        else:
            return format_html('<input class="form-check-input status-toggle" type="checkbox" id="flexCheckDefault" data-partners-id="{}">', record.id)

class ResourceTable(tables.Table):

    id = tables.Column(verbose_name='ID', attrs={"td":{"width":"5%"}})
    #В user_id ссылка LinkColumn на страницу Аси "Информация о партнере" страница partner_information_form
    user_id = tables.Column(accessor='user_id.full_name', order_by=('user_id.first_name', 'user_id.last_name'), verbose_name='Ответственный', attrs={"td":{"width":"15%"}})
    status = tables.Column(verbose_name='Статус', attrs={'th':{'scope':'col'}, "td":{"width":"20%"}}) 
    check = tables.BooleanColumn(verbose_name='', attrs={'th':{'scope':'col'}, "td":{"width":"20%"}})
    # paginate_by = 10
    class Meta:
        model = Resource
        attrs = {"class": "table table-layout-fixed"}
        exclude = ('type_id','requirements','ticket_status', 'id_metaservice', 
                   'is_global', 'is_visible')

    def render_check(self, value, record):
        if record.status == 'active':
            return format_html('<input class="form-check-input status-toggle" checked type="checkbox" id="flexCheckDefault" data-resource-id="{}">', record.id)
        else:
            return format_html('<input class="form-check-input status-toggle" type="checkbox" id="flexCheckDefault" data-resource-id="{}">', record.id)

    