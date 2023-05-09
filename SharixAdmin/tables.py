import django_tables2 as tables
from metaservicesynced.models import *
from .models import *
from django.utils.html import format_html
from metaservicesynced.models import *


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

class ProviderTable(tables.Table):

    id = tables.Column(verbose_name='ID', attrs={"td":{"width":"5%"}})
    user_id = tables.Column(accessor='user_id.full_name', order_by=('user_id.first_name', 'user_id.last_name'), verbose_name='ФИО', attrs={"td":{"width":"15%"}})

    status = tables.Column(verbose_name='Статус', attrs={'th':{'scope':'col'}, "td":{"width":"20%"}}) 
    check = tables.BooleanColumn(verbose_name='', attrs={'th':{'scope':'col'}, "td":{"width":"20%"}})
    paginate_by = 10
    class Meta:
        model = Provider
        attrs = {"class": "table table-layout-fixed"}
        exclude = ('type','company_id','id_metaservice', 'requirements', 
                   'ticket_status', 'location_type', 'default_location', 
                   'is_global', 'is_visible')

    def render_check(self, value, record):
        if record.status == 'active':
            return format_html('<input class="form-check-input status-toggle" checked type="checkbox" id="flexCheckDefault" data-provider-id="{}">', record.id)
        else:
            return format_html('<input class="form-check-input status-toggle" type="checkbox" id="flexCheckDefault" data-provider-id="{}">', record.id)

class ServiceTariffTable(tables.Table):

    id = tables.Column(verbose_name='ID', attrs={"td":{"width":"5%"}})
    servicetype_id = tables.LinkColumn('service_tariff/edit/', verbose_name='Название тарифа', text = lambda record: record.servicetype_id.caption,
        args=[tables.A('pk')], attrs={'th':{'scope':'col'}, "td":{"width":"20%"}})
    ticket_status = tables.Column(verbose_name='Название схемы услуги', attrs={'th':{'scope':'col'}, "td":{"width":"20%"}}) 
    check = tables.BooleanColumn(verbose_name='Активность', orderable=False, attrs={'th':{'scope':'col'}, "td":{"width":"20%"}})


    class Meta:
        model = Service
        attrs = {"class": "table table-layout-fixed"}
        exclude = ('resource_id','id_provider','price_alg',
                   'price_min','price_amount','id_metaservice', 
                   'requirements', 'service_status', 'price_km',
                   'is_global', 'is_visible','status')

    def render_check(self, value, record):
        if record.status == 'active':
            return format_html('<input class="form-check-input status-toggle" disabled  checked type="checkbox"')
        else:
            return format_html('<input class="form-check-input status-toggle" disabled  type="checkbox"')

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
        
    def render_name_operation(self, value, record):
        return format_html("<a href='{}'>{}</a>", record.get_absolute_url(), value)
   
class ServiceTable(tables.Table):

    id = tables.Column(verbose_name='ID', attrs={"td":{"width":"5%"}})
    servicetype_id = tables.Column(verbose_name='Описание услуги (сервиса)', accessor = 'servicetype_id.caption',
        attrs={'th':{'scope':'col'}, "td":{"width":"20%"}})
    
    # description = tables.Column(verbose_name='Название тарифа', attrs={'th':{'scope':'col'}, "td":{"width":"20%"}})
    # description = tables.Column(verbose_name='Описание строки тарифов', attrs={'th':{'scope':'col'}, "td":{"width":"20%"}})
    # price_type = tables.Column(verbose_name='Тип тарифа', attrs={'th':{'scope':'col'}, "td":{"width":"20%"}})
    
    price_km = tables.Column(verbose_name='Стоимость км.', attrs={'th':{'scope':'col'}, "td":{"width":"20%"}})
    price_min = tables.Column(verbose_name='Стоимость мин.', attrs={'th':{'scope':'col'}, "td":{"width":"20%"}})
    price_amount = tables.Column(verbose_name='Стоимость услуги', attrs={'th':{'scope':'col'}, "td":{"width":"20%"}})

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

class UserInfoTable(tables.Table):

    id = tables.Column(verbose_name='ID', attrs={"td":{"width":"5%"}})

    class Meta:
        model = SharixUser
        attrs = {"class": "table table-layout-fixed"}
        exclude = ('password', 'phone_number', 
                   'last_login','is_staff', 'is_superuser',
                   'date_joined')