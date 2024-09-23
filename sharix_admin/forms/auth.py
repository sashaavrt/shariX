from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth import get_user_model

from sharix_admin.forms import BaseForm


class ShariXSignUpForm(BaseForm, UserCreationForm):
    """
    Форма для регистрации пользователей.
    """
    class Meta:
        model = get_user_model()
        fields = ('last_name', 'first_name', 'middle_name', 'phone_number', 'email', 'username')


class ShariXLoginForm(BaseForm, AuthenticationForm):
    """
    Форма для авторизации пользователей.
    """
    pass