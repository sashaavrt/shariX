from dbsynce.models import ServiceType, Service, Company
from django import forms


class ServiceTariffUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiceTariffUpdateForm, self).__init__(*args, **kwargs)

        # Добавляет стиль бутстрапа form-control всем полям таблицы если у них нет своих стилей
        for field in iter(self.fields):
            if 'class' not in self.fields[field].widget.attrs:
                self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:

        model = Service
        fields = [
            'status',
            'ticket_status',
            'servicetype',
            'resource',
            'requirements',
            'price_alg',
            'price_km',
            'price_min',
            'price_amount',
            'service_status',
            'is_global',
            'is_visible'
        ]
        widgets = {
            'status': forms.TextInput(attrs={'readonly': True}, ),
            'ticket_status': forms.TextInput(attrs={'readonly': True}),

            'servicetype': forms.Select(attrs={'class': 'form-select'}),
            'resource': forms.Select(attrs={'class': 'form-select'}),
        }


class ServiceTariffCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiceTariffCreateForm, self).__init__(*args, **kwargs)
        # Добавляет стиль бутстрапа form-control всем полям таблицы если у них нет своих стилей
        for field in iter(self.fields):
            if 'class' not in self.fields[field].widget.attrs:
                self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:

        model = Service
        fields = '__all__'

        widgets = {
            'servicetype': forms.Select(attrs={'class': 'form-select'}),
            'resource': forms.Select(attrs={'class': 'form-select'}),
            'ticket_status': forms.TextInput(attrs={'readonly': True}),
        }


class ServiceTypeUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiceTypeUpdateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ServiceType
        fields = [
            'status',
            'ticket_status',
            'id_metaservice',
            'codename',
            'description',
            'requirements',
            'price_type',
            'link_agreement',
            'is_global',
            'is_visible'
        ]
        widgets = {
            'status': forms.TextInput(attrs={'readonly': True}),
            'ticket_status': forms.TextInput(attrs={'readonly': True}),
        }


PRICE_CHOICES = [
    ('one', 'text #1'),
    ('two', 'text #2'),
    ('three', 'text #3'),
]


class ServiceTypeCreateForm(forms.ModelForm):
    codename = forms.CharField(label="Название услуги")
    requirements = forms.CharField(label="Требования")
    price_type = forms.ChoiceField(choices=PRICE_CHOICES, label="Ценообразование")
    description = forms.CharField(label="Описание")
    is_global = forms.BooleanField(label="Доступно во всех сервисах", required=False)
    is_visible = forms.BooleanField(label="Доступно для планирования цепочек во всех сервисах", required=False)

    def __init__(self, *args, **kwargs):
        super(ServiceTypeCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ServiceType
        fields = [
            'codename',
            'requirements',
            'price_type',
            'description',
            'is_global',
            'is_visible',
        ]

        widgets = {

        }


class ServiceInformationUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ServiceInformationUpdateForm, self).__init__(*args, **kwargs)
        # Добавляет стиль бутстрапа form-control всем полям таблицы если у них нет своих стилей
        for field in iter(self.fields):
            if 'class' not in self.fields[field].widget.attrs:
                self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Service
        fields = [
            'servicetype'
        ]

        widgets = {
            # 'status': forms.TextInput(attrs={'readonly': True}),
            # 'ticket_status': forms.TextInput(attrs={'readonly': True}),

            'servicetype': forms.Select(attrs={'class': 'form-select'}),
            # 'repr': forms.Select(attrs={'class': 'form-select'}),
            # 'resource': forms.Select(attrs={'class': 'form-select'}),
        }


class ServiceInformationCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ServiceInformationCreateForm, self).__init__(*args, **kwargs)
        # Добавляет стиль бутстрапа form-control всем полям таблицы если у них нет своих стилей
        for field in iter(self.fields):
            if 'class' not in self.fields[field].widget.attrs:
                self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Service
        fields = "__all__"
        exclude = [
            "id",
            "is_global",
            "is_visible",
            "ticket_status",
            "id_metaservice",
            "resource"
        ]

        widgets = {
            # 'servicetype': forms.CharField(max_length=255)
            # 'legal_name': forms.TextInput(label = 'Название')
            # 'servicetype': forms.Select(attrs={'class': 'form-select'}),
            # 'repr': forms.Select(attrs={'class': 'form-select'}),
            # 'resource': forms.Select(attrs={'class': 'form-select'}),
            # 'ticket_status': forms.Select(attrs={'class': 'form-select'}),
        }


class PartnerInformationUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PartnerInformationUpdateForm, self).__init__(*args, **kwargs)
        # Добавляет стиль бутстрапа form-control всем полям таблицы если у них нет своих стилей
        for field in iter(self.fields):
            if 'class' not in self.fields[field].widget.attrs:
                self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Company
        fields = "__all__"
        exclude = [
            "id",
            "ticket_status",
            "is_global",
            "is_visible",
            "id_metaservice",
            "status"
        ]
        widgets = {
            'description': forms.Select(attrs={'class': 'form-select'}),
            'repr': forms.Select(attrs={'class': 'form-select'}),
        }


class PartnerInformationCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PartnerInformationCreateForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if 'class' not in self.fields[field].widget.attrs:
                self.fields[field].widget.attrs.update({'class': 'form-control'})

    # legal_name = forms.Fi()
    class Meta:
        model = Company
        fields = "__all__"
        exclude = [
            "id",
            "ticket_status",
            "is_global",
            "is_visible",
            "id_metaservice",
            "status"
        ]

        widgets = {
            'description': forms.Select(attrs={'class': 'form-select'}),
            'repr': forms.Select(attrs={'class': 'form-select'}),
        }

        #     username = forms.CharField(label="Номер телефона",
        # widget=forms.TextInput(attrs={'class':'form-control'}))
