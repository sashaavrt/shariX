from django_tables2 import SingleTableView
from SharixAdmin.tables import ProviderTable
from metaservicesynced.models import Provider
from django.contrib.auth.decorators import login_required
from SharixAdmin.views.context import get_context
from django.http import JsonResponse

class ProviderListView(SingleTableView):
    table_class = ProviderTable
    queryset = Provider.objects.all()
    template_name = 'SharixAdmin/provider.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': 'Исполнители',
            'object_list': context['object_list'],
        }))
        return context
    
@login_required
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