from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import Group

from sharix_admin.forms.base import BaseForm


class ShariXSignUpForm(BaseForm, UserCreationForm):
    """
    Форма для регистрации пользователей. 
    """

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['phone_number']  # FIXME: Имя пользователя = номер телефона
        if commit:
            user.save()
            user.groups.add(Group.objects.get(id=51))  # Добавляем всех пользователей по умолчанию в группу CLIENT
        return user

    class Meta:
        model = get_user_model()
        fields = ('last_name', 'first_name', 'middle_name', 'phone_number', 'email')
        labels = {
            'middle_name': 'Отчество (не обязательно)',
            'phone_number': 'Номер телефона (только цифры)',
        }


class ShariXLoginForm(BaseForm, AuthenticationForm):
    """
    Форма для авторизации пользователей.
    """
    pass
