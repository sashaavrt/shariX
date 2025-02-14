from dbsynce.models import Resource
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import JsonResponse
from django.utils.translation import gettext as _
from django_tables2 import SingleTableView

from sharix_admin.tables import ResourceTable
from sharix_admin.utils import group_required


class ResourceListView(UserPassesTestMixin, SingleTableView):
    table_class = ResourceTable
    queryset = Resource.objects.all()
    template_name = 'sharix_admin/resource.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': _('Resources'),
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
def change_resource_status(request):
    if request.method == 'POST':
        resource = request.POST.get('resource')
        new_status = request.POST.get('new_status')

        resource = Resource.objects.get(pk=resource)
        resource.status = new_status
        resource.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})
