from django.http import HttpResponseRedirect
from SharixAdmin.forms import LoginUserForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('authweb'))

class LoginSharix(LoginView):
    form_class = LoginUserForm
    template_name = 'SharixAdmin/auth.html'

    
    def get_success_url(self):
        print(self.request.GET['next'])
        
        return reverse_lazy('home')