from django.contrib.auth.forms import AuthenticationForm

from metaservicesynced.models import *
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
        

class PartnerInformationUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PartnerInformationUpdateForm, self).__init__(*args, **kwargs)
        # Добавляет стиль бутстрапа form-control всем полям таблицы если у них нет своих стилей
        for field in iter(self.fields):
            if 'class' not in self.fields[field].widget.attrs:
                self.fields[field].widget.attrs.update({'class':'form-control'})

    class Meta:
        model = Company
        fields = ['legal_name', 'address', 'repr_id' ]
        widgets = {
            'description': forms.Select(attrs={'class': 'form-select'}),
            'repr_id': forms.Select(attrs={'class': 'form-select'}),
        }
        
class PartnerInformationCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PartnerInformationCreateForm, self).__init__(*args, **kwargs)
        # Добавляет стиль бутстрапа form-control всем полям таблицы если у них нет своих стилей
        for field in iter(self.fields):
            if 'class' not in self.fields[field].widget.attrs:
                self.fields[field].widget.attrs.update({'class':'form-control'})
                
    class Meta:
        model = Company
        fields = ['legal_name', 'address', 'repr_id']
        
        widgets = {
            'description': forms.Select(attrs={'class': 'form-select'}),
            'repr_id': forms.Select(attrs={'class': 'form-select'}),
        }