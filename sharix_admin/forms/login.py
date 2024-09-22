from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


class LoginUserForm(AuthenticationForm):
    password = forms.CharField(label="Пароль",
        widget=forms.PasswordInput(attrs={'class':'form-control'}))

    username = forms.CharField(label="Номер телефона",
        widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']