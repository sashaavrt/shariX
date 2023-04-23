from django.contrib.auth.forms import AuthenticationForm
from .models import SharixUser
from django import forms
from metaservicesynced.models import ServiceType

class LoginUserForm(AuthenticationForm):

    password = forms.CharField(label="Пароль",
        widget=forms.PasswordInput(attrs={'class':'form-control'}))

    username = forms.CharField(label="Номер телефона",
        widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = SharixUser
        fields = ['username', 'password']


class ServiceTypeUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiceTypeUpdateForm, self).__init__(*args, **kwargs)
        # Добавляет стиль бутстрапа form-control всем полям таблицы если у них нет своих стилей
        for field in iter(self.fields):
            if 'class' not in self.fields[field].widget.attrs:
                self.fields[field].widget.attrs.update({'class':'form-control'})

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
        # Добавляет стиль бутстрапа form-control всем полям таблицы если у них нет своих стилей
        for field in iter(self.fields):
            if 'class' not in self.fields[field].widget.attrs:
                self.fields[field].widget.attrs.update({'class':'form-control'})
    
    class Meta:
        model = ServiceType
        fields = '__all__'

        widgets = {
            'ticket_status': forms.Select(attrs={'class': 'form-select'}),
        }
