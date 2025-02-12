import django_tables2 as tables
from dbsynce.models import *
from dbsynce.models import *
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _


class TransactionsWalletTable(tables.Table):
    # id = tables.Column(order_by=True)
    id = tables.Column(
        verbose_name='#',
        orderable=False,
        attrs={
            "td": {"width": "5%"}
        }
    )
    wallet = tables.Column(
        verbose_name=_('Owner'),
        orderable=False,
        attrs={
            "td": {"width": "15%"}
        }
    )
    name_operation = tables.Column(
        verbose_name=_('Service'),
        attrs={
            'th': {'scope': 'col'},
            "td": {"width": "20%"}
        }
    )
    price = tables.Column(
        verbose_name=_('Points'),
        attrs={
            "class": "row",
            "td": {"width": "10%"}
        }
    )
    date_operation = tables.Column(
        verbose_name=_('Registration date'),
        attrs={
            "td": {"width": "30%"}
        }
    )
    is_carried_out = tables.BooleanColumn(
        verbose_name=_('Status'),
        orderable=False,
        yesno=_("Successful, not successful"),
        attrs={
            "td": {"width": "20%"}
        }
    )

    class Meta:
        # model = TransactionsWallets
        attrs = {
            "class": "table table-striped"
        }
        exclude = (
            "balance_before",
            "amount",
            "metaservice_id",
            "transaction_type",
            "doc_num",
            "service_id"
        )

    def render_name_operation(self, value, record):
        return format_html(
            "<a href='{}'>{}</a>",
            record.get_absolute_url(),
            value
        )


class PartnersTable(tables.Table):
    id = tables.Column(
        verbose_name=_('ID'),
        attrs={
            "td": {"width": "5%"}
        }
    )
    legal_name = tables.Column(
        verbose_name=_('Legal entity'),
        attrs={
            'th': {'scope': 'col'},
            "td": {"width": "20%"}
        }
    )
    repr_id = tables.Column(
        accessor='repr_id.full_name',
        order_by=('repr_id.first_name', 'repr_id.last_name'),
        verbose_name=_('Responsible'),
        attrs={
            "td": {"width": "15%"}
        }
    )
    status = tables.Column(
        verbose_name=_('Status'),
        attrs={
            'th': {'scope': 'col'},
            "td": {"width": "20%"}
        }
    )
    check = tables.BooleanColumn(
        verbose_name='',
        attrs={
            'th': {'scope': 'col'},
            "td": {"width": "20%"}
        }
    )

    # paginate_by = 10
    class Meta:
        model = Company
        attrs = {
            "class": "table table-layout-fixed"
        }
        exclude = (
            'inn',
            'kpp',
            'ogrn',
            'bank_name',
            'bik',
            'ks',
            'rs',
            'address',
            'requirements',
            'id_metaservice',
            'is_global',
            'is_visible',
            'ticket_status'
        )

    def render_check(self, value, record):
        if record.status == 'active':
            return format_html(
                '<input class="form-check-input status-toggle" checked type="checkbox" id="flexCheckDefault" data-partners-id="{}">',
                record.id
            )
        else:
            return format_html(
                '<input class="form-check-input status-toggle" type="checkbox" id="flexCheckDefault" data-partners-id="{}">',
                record.id
            )


class ResourceTable(tables.Table):
    id = tables.Column(
        verbose_name=_('ID'),
        attrs={
            "td": {"width": "5%"}
        }
    )
    # В user_id ссылка LinkColumn на страницу Аси "Информация о партнере" страница partner_information_form
    user_id = tables.Column(
        accessor='user_id.full_name',
        order_by=('user_id.first_name', 'user_id.last_name'),
        verbose_name=_('Responsible'),
        attrs={
            "td": {"width": "15%"}
        }
    )
    status = tables.Column(
        verbose_name=_('Status'),
        attrs={
            'th': {'scope': 'col'},
            "td": {"width": "20%"}
        }
    )
    check = tables.BooleanColumn(
        verbose_name='',
        attrs={
            'th': {'scope': 'col'},
            "td": {"width": "20%"}
        }
    )

    # paginate_by = 10
    class Meta:
        model = Resource
        attrs = {
            "class": "table table-layout-fixed"
        }
        exclude = (
            'id_metaservice',
            'resoure_type',
            'requirements',
            'is_global',
            'is_visible',
            'ticket_status'
        )

    def render_check(self, value, record):
        if record.status == 'active':
            return format_html(
                '<input class="form-check-input status-toggle" checked type="checkbox" id="flexCheckDefault" data-resource-id="{}">',
                record.id
            )
        else:
            return format_html(
                '<input class="form-check-input status-toggle" type="checkbox" id="flexCheckDefault" data-resource-id="{}">',
                record.id
            )


class ProviderTable(tables.Table):
    id = tables.Column(
        verbose_name=_('ID'),
        attrs={
            "td": {"width": "5%"}
        }
    )
    user_id = tables.Column(
        accessor='user_id.full_name',
        order_by=('user_id.first_name', 'user_id.last_name'),
        verbose_name=_('Full Name'),
        attrs={
            "td": {"width": "15%"}
        }
    )
    status = tables.Column(
        verbose_name=_('Status'),
        attrs={
            'th': {'scope': 'col'},
            "td": {"width": "20%"}
        }
    )
    check = tables.BooleanColumn(
        verbose_name='',
        attrs={
            'th': {'scope': 'col'},
            "td": {"width": "20%"}
        }
    )
    paginate_by = 10

    class Meta:
        model = Provider
        attrs = {
            "class": "table table-layout-fixed"
        }
        exclude = (
            'type',
            'company_id',
            'id_metaservice',
            'requirements',
            'ticket_status',
            'location_type',
            'default_location',
            'is_global',
            'is_visible'
        )

    def render_check(self, value, record):
        if record.status == 'active':
            return format_html(
                '<input class="form-check-input status-toggle" checked type="checkbox" id="flexCheckDefault" data-provider-id="{}">',
                record.id
            )
        else:
            return format_html(
                '<input class="form-check-input status-toggle" type="checkbox" id="flexCheckDefault" data-provider-id="{}">',
                record.id
            )


class ServiceTariffTable(tables.Table):
    id = tables.Column(
        verbose_name=_('ID'),
        attrs={
            "td": {"width": "5%"}
        }
    )
    servicetype_id = tables.LinkColumn(
        'service_tariff/edit/',
        verbose_name=_('Name of the tariff'),
        text=lambda record: record.servicetype_id.caption,
        args=[tables.A('pk')],
        attrs={
            'th': {'scope': 'col'},
            "td": {"width": "20%"}
        }
    )
    ticket_status = tables.Column(
        verbose_name=_('Name of the service scheme'),
        attrs={
            'th': {'scope': 'col'},
            "td": {"width": "20%"}
        }
    )
    check = tables.BooleanColumn(
        verbose_name=_('Activity'),
        orderable=False,
        attrs={
            'th': {'scope': 'col'},
            "td": {"width": "20%"}
        }
    )

    class Meta:
        model = Service
        attrs = {
            "class": "table table-layout-fixed"
        }
        exclude = (
            'resource_id',
            'price_alg',
            'price_min',
            'price_amount',
            'id_metaservice',
            'requirements',
            'service_status',
            'price_km',
            'is_global',
            'is_visible',
            'status'
        )

    def render_check(self, value, record):
        if record.status == 'active':
            return format_html('<input class="form-check-input status-toggle" disabled  checked type="checkbox"')
        else:
            return format_html('<input class="form-check-input status-toggle" disabled  type="checkbox"')


class ServiceTypeTable(tables.Table):
    id = tables.Column(attrs={"td": {"width": "50px"}})
    codename = tables.LinkColumn(
        'service_type/edit/',
        verbose_name='Услуга',
        orderable=False,
        text=lambda record: record.codename,
        args=[tables.A('pk')],
        attrs={
            "a": {"style": "pointer-events: none;"},
            'th': {'scope': 'col'},
            "td": {"class": "name_col"}
        }
    )
    description = tables.LinkColumn(
        'service_type/edit/',
        orderable=False, verbose_name='Описание',
        text=lambda record: record.description,
        args=[tables.A('pk')],
        attrs={
            "a": {"style": "pointer-events: none;"},
            'th': {'scope': 'col'},
            "td": {"class": "description_col"}
        }
    )
    edit = tables.LinkColumn(
        'service_type/edit/',
        verbose_name='',
        orderable=False,
        text="E",
        args=[tables.A('pk')],
        attrs={
            'th': {'scope': 'col'},
            "td": {"class": "edit_col"}
        }
    )
    deletee = tables.LinkColumn(
        'service_type/delete/',
        verbose_name='',
        orderable=False,
        text="D",
        args=[tables.A('pk')],
        attrs={
            'th': {'scope': 'col'},
            "td": {"class": "delete_col"}
        }
    )

    class Meta:
        model = ServiceType
        attrs = {
            "class": "table table-layout-fixed text-start"
        }
        exclude = (
            'requirements',
            'price_type',
            'status',
            'ticket_status',
            'id_metaservice',
            'link_agreement',
            'is_global',
            'is_visible',
            'caption'
        )

    # def render_delete(self, value, record):
    #     return format_html('<a href="/service_type/delete" class="btn btn-outline-danger">_(Delete)</a>')

    # def render_name_operation(self, value, record):
    #     return format_html("<a href='{}'>{}</a>", record.get_absolute_url(), value)


class ServiceTable(tables.Table):
    id = tables.Column(
        verbose_name=_('ID'),
        attrs={
            "td": {"width": "5%"}
        }
    )
    servicetype_id = tables.Column(
        verbose_name=_('Description of the service'),
        accessor='servicetype_id.caption',
        attrs={
            'th': {'scope': 'col'},
            "td": {"width": "20%"}}
    )

    # description = tables.Column(verbose_name='Название тарифа', attrs={'th':{'scope':'col'}, "td":{"width":"20%"}})
    # description = tables.Column(verbose_name='Описание строки тарифов', attrs={'th':{'scope':'col'}, "td":{"width":"20%"}})
    # price_type = tables.Column(verbose_name='Тип тарифа', attrs={'th':{'scope':'col'}, "td":{"width":"20%"}})

    price_km = tables.Column(
        verbose_name=_('Cost km.'),
        attrs={
            'th': {'scope': 'col'},
            "td": {"width": "20%"}
        }
    )
    price_min = tables.Column(
        verbose_name=_('Cost min.'),
        attrs={
            'th': {'scope': 'col'},
            "td": {"width": "20%"}}
    )
    price_amount = tables.Column(
        verbose_name=_('Cost of service'),
        attrs={
            'th': {'scope': 'col'},
            "td": {"width": "20%"}
        }
    )

    class Meta:
        model = Service
        attrs = {
            "class": "table table-layout-fixed"
        }
        exclude = (
            'resource_id',
            'requirements',
            'id_metaservice',
            'price_alg',
            'service_status',
            'ticket_status',
            'is_global',
            'is_visible'
        )

    def render_check(self, value, record):
        if record.status == 'active':
            return format_html(
                '<input class="form-check-input status-toggle" checked type="checkbox" id="flexCheckDefault" data-service-id="{}">',
                record.id
            )
        else:
            return format_html(
                '<input class="form-check-input status-toggle" type="checkbox" id="flexCheckDefault" data-service-id="{}">',
                record.id
            )


class UserInfoTable(tables.Table):
    id = tables.Column(
        verbose_name=_('ID'),
        attrs={
            "td": {"width": "5%"}
        }
    )

    class Meta:
        model = get_user_model()
        attrs = {
            "class": "table table-layout-fixed"
        }
        exclude = (
            'password',
            'phone_number',
            'last_login',
            'is_staff',
            'is_superuser',
            'date_joined'
        )
