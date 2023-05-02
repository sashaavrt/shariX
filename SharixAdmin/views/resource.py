from django_tables2 import SingleTableView
from SharixAdmin.tables import ResourceTable
from django.contrib.auth.decorators import login_required
from metaservicesynced.models import Resource
from SharixAdmin.views.context import get_context
from django.http import JsonResponse

class ResourceListView(SingleTableView):
    table_class = ResourceTable
    queryset = Resource.objects.all()
    template_name = 'SharixAdmin/resource.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': 'Ресурсы',
            'object_list': context['object_list'],
        }))
        return context
    

@login_required
def change_resource_status(request):
    if request.method == 'POST':
        resource_id = request.POST.get('resource_id')
        new_status = request.POST.get('new_status')
        
        resource = Resource.objects.get(pk=resource_id)
        resource.status = new_status
        resource.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})