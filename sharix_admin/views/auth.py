from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from sharix_admin.forms import ShariXSignUpForm, ShariXLoginForm


class ShariXSignUpView(CreateView):
    """
    Представление для регистрации пользователей.
    """
    form_class = ShariXSignUpForm
    template_name = 'sharix_admin/auth/signup.html'
    success_url = reverse_lazy('sharix_admin:auth_login')


class ShariXLoginView(LoginView):
    """
    Представление для входа в систему.
    """
    form_class = ShariXLoginForm
    template_name = "sharix_admin/auth/login.html"
    redirect_authenticated_user = True


# FIXME: Восстановления паролей сейчас не работает. Установлена заглушка.
class ShariXResetPasswordView(TemplateView):
    """
    Представление для восстановления пароля.
    """
    template_name = "sharix_admin/auth/reset_password.html"
