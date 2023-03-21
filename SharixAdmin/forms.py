from django.contrib.auth.forms import AuthenticationForm
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