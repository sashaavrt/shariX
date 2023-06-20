from django.contrib.auth.forms import AuthenticationForm

from metaservicesynced.models import *
from .models import SharixUser
from django import forms
from metaservicesynced.models import ServiceType, Service
from .models import SharixUser
from django import forms

class LoginUserForm(AuthenticationForm):

    password = forms.CharField(label="Пароль",
        widget=forms.PasswordInput(attrs={'class':'form-control'}))

    username = forms.CharField(label="Номер телефона",
        widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = SharixUser
        fields = ['username', 'password']


class ServiceTariffUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiceTariffUpdateForm, self).__init__(*args, **kwargs)

        # Добавляет стиль бутстрапа form-control всем полям таблицы если у них нет своих стилей
        for field in iter(self.fields):
            if 'class' not in self.fields[field].widget.attrs:
                self.fields[field].widget.attrs.update({'class':'form-control'})

    class Meta:

        model = Service
        fields = ['status','ticket_status','servicetype_id','id_provider',
                  'resource_id','requirements','price_alg','price_km','price_min','price_amount','service_status',
                  'is_global','is_visible']
        widgets = {
            'status': forms.TextInput(attrs={'readonly': True}, ),
            'ticket_status': forms.TextInput(attrs={'readonly': True}),
            
            'servicetype_id': forms.Select(attrs={'class': 'form-select'}),
            'id_provider': forms.Select(attrs={'class': 'form-select'}),
            'resource_id': forms.Select(attrs={'class': 'form-select'}),
        }

class ServiceTariffCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiceTariffCreateForm, self).__init__(*args, **kwargs)
        # Добавляет стиль бутстрапа form-control всем полям таблицы если у них нет своих стилей
        for field in iter(self.fields):
            if 'class' not in self.fields[field].widget.attrs:
                self.fields[field].widget.attrs.update({'class':'form-control'})
    
    class Meta:

        model = Service
        fields = '__all__'

        widgets = {
            'servicetype_id': forms.Select(attrs={'class': 'form-select'}),
            'id_provider': forms.Select(attrs={'class': 'form-select'}),
            'resource_id': forms.Select(attrs={'class': 'form-select'}),
            'ticket_status': forms.Select(attrs={'class': 'form-select'}),
        }

class ServiceTypeUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiceTypeUpdateForm, self).__init__(*args, **kwargs)
    class Meta:
        model = ServiceType
        fields = ['status','ticket_status','id_metaservice','codename',
                  'description','requirements','price_type','link_agreement',
                  'is_global','is_visible']
        widgets = {
            'status': forms.TextInput(attrs={'readonly': True}),
            'ticket_status': forms.TextInput(attrs={'readonly': True}),
        }

class ServiceTypeCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiceTypeCreateForm, self).__init__(*args, **kwargs)
    class Meta:
        model = ServiceType
        fields = '__all__'

        widgets = {
            'ticket_status': forms.Select(attrs={'class': 'form-select'}),
        }

class ServiceInformationUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ServiceInformationUpdateForm, self).__init__(*args, **kwargs)
        # Добавляет стиль бутстрапа form-control всем полям таблицы если у них нет своих стилей
        for field in iter(self.fields):
            if 'class' not in self.fields[field].widget.attrs:
                self.fields[field].widget.attrs.update({'class':'form-control'})
        
    
    class Meta:
        model = Service
        fields = ['servicetype_id', 'id_provider']

        widgets = {
            # 'status': forms.TextInput(attrs={'readonly': True}),
            # 'ticket_status': forms.TextInput(attrs={'readonly': True}),
            
             'servicetype_id': forms.Select(attrs={'class': 'form-select'}),
            #'repr_id': forms.Select(attrs={'class': 'form-select'}),
            # 'resource_id': forms.Select(attrs={'class': 'form-select'}),
        }
        
class ServiceInformationCreateForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ServiceInformationCreateForm, self).__init__(*args, **kwargs)
        # Добавляет стиль бутстрапа form-control всем полям таблицы если у них нет своих стилей
        for field in iter(self.fields):
            if 'class' not in self.fields[field].widget.attrs:
                self.fields[field].widget.attrs.update({'class':'form-control'})


    class Meta:
        model = Service
        fields = "__all__"
        exclude = ["id", 
                   "is_global", 
                   "is_visible", 
                   "ticket_status",
                   "id_metaservice",
                   "resource_id"]

        widgets = {
            #'servicetype_id': forms.CharField(max_length=255)
            # 'legal_name': forms.TextInput(label = 'Название')
            # 'servicetype_id': forms.Select(attrs={'class': 'form-select'}),
            #'repr_id': forms.Select(attrs={'class': 'form-select'}),
            # 'resource_id': forms.Select(attrs={'class': 'form-select'}),
            # 'ticket_status': forms.Select(attrs={'class': 'form-select'}),
        }

class PartnerInformationUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PartnerInformationUpdateForm, self).__init__(*args, **kwargs)
        # Добавляет стиль бутстрапа form-control всем полям таблицы если у них нет своих стилей
        for field in iter(self.fields):
            if 'class' not in self.fields[field].widget.attrs:
                self.fields[field].widget.attrs.update({'class':'form-control'})

    class Meta:
        model = Company
        fields = "__all__"
        exclude = ["id", "ticket_status",
                   "is_global", 
                   "is_visible", 
                   "id_metaservice",
                   ]
        widgets = {
            'description': forms.Select(attrs={'class': 'form-select'}),
            'repr_id': forms.Select(attrs={'class': 'form-select'}),
        }
        
class PartnerInformationCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PartnerInformationCreateForm, self).__init__(*args, **kwargs)       
        for field in iter(self.fields):
            if 'class' not in self.fields[field].widget.attrs:
                self.fields[field].widget.attrs.update({'class':'form-control'})
   
    # legal_name = forms.Fi()
    class Meta:
        model = Company
        fields = "__all__"
        exclude = ["id", "ticket_status",
                   "is_global", 
                   "is_visible", 
                   "id_metaservice",
                   ]

        widgets = {
            'description': forms.Select(attrs={'class': 'form-select'}),
            'repr_id': forms.Select(attrs={'class': 'form-select'}),
        }


        #     username = forms.CharField(label="Номер телефона",
        # widget=forms.TextInput(attrs={'class':'form-control'}))