from django_tables2 import SingleTableView
from SharixAdmin.groups import group_required
from SharixAdmin.tables import ServiceTable
from metaservicesynced.models import Service
from django.contrib.auth.decorators import login_required
from SharixAdmin.views.context import get_context
from django.contrib.auth.mixins import UserPassesTestMixin

class ServiceListView(UserPassesTestMixin, SingleTableView):
    table_class = ServiceTable
    queryset = Service.objects.all()
    template_name = 'SharixAdmin/service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': 'Тарифы',
            'object_list': context['object_list'],
        }))
        return context
    
    def test_func(self) -> bool or None:
        group_names = ('PARTNER-ADMIN')
        if bool(self.request.user.groups.filter(name=group_names)) or self.request.user.is_superuser:
            return True
        return False

@login_required
@group_required('PARTNER-ADMIN')
def change_service_status(request):
    if request.method == 'POST':
        service_id = request.POST.get('service_id')
        new_status = request.POST.get('new_status')
        
        service = Service.objects.get(pk=service_id)
        service.status = new_status
        service.save()