from django_tables2 import SingleTableView
from sharix_admin.utils import group_required
from sharix_admin.tables import ProviderTable
from dbsynce.models import Provider
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils.translation import gettext as _

class ProviderListView(UserPassesTestMixin, SingleTableView):
    table_class = ProviderTable
    queryset = Provider.objects.all()
    template_name = 'sharix_admin/provider.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': _('Performers'),
            'object_list': context['object_list'],
        })
        return context
    
    def test_func(self) -> bool or None:
        group_names = ('PARTNER-ADMIN')
        if bool(self.request.user.groups.filter(name=group_names)) or self.request.user.is_superuser:
            return True
        return False

    
@login_required
@group_required('PARTNER-ADMIN')
def change_provider_status(request):
    if request.method == 'POST':
        provider_id = request.POST.get('provider_id')
        new_status = request.POST.get('new_status')
        
        provider = Provider.objects.get(pk=provider_id)
        provider.status = new_status
        provider.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})