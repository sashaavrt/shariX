from django.shortcuts import render
from SharixAdmin.forms import PartnerInformationCreateForm, PartnerInformationUpdateForm
from metaservicesynced.models import Company
from django.views.generic.edit import UpdateView, CreateView
from SharixAdmin.views.context import get_context
from django.urls import reverse

class PartnerInformationCreate(CreateView):
    model = Company
    form_class = PartnerInformationCreateForm
    template_name = "SharixAdmin/partner_information_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': 'Информация о партнере',
            'object': self.object,
        }))
        return context
    
    def get_success_url(self):
        return reverse('test-page')
    
class PartnerInformationUpdateView(UpdateView):
    model = Company
    form_class = PartnerInformationUpdateForm
    template_name = "SharixAdmin/partner_information_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': 'Информация о партнере',
            'object': self.object,
        }))
        return context
    
    def get_success_url(self):
        return reverse('test-page')
    
def partner_information(request):
    context = get_context(request, {
        'title':'Информация о партнере',
        })
    
    return render(request, 'SharixAdmin/partner_information.html', context)