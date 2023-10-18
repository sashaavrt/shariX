from django_tables2 import SingleTableView
from django.contrib.auth.mixins import UserPassesTestMixin
from SharixAdmin.groups import group_required
from SharixAdmin.tables import PartnersTable
from django.contrib.auth.decorators import login_required
from metaservicesynced.models import Company
from SharixAdmin.views.context import get_context
from django.http import JsonResponse
from django.utils.translation import gettext as _


class PartnersListView(UserPassesTestMixin, SingleTableView):
    table_class = PartnersTable
    queryset = Company.objects.all()
    template_name = 'SharixAdmin/partners.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context(self.request, {
            'title': _('Partners'),
            'object_list': context['object_list'],
        }))
        return context
    
    def test_func(self) -> bool or None:
        group_names = ('METASERVICE-ADMIN')
        if bool(self.request.user.groups.filter(name=group_names)) or self.request.user.is_superuser:
            return True
        return False

@login_required
@group_required('METASERVICE-ADMIN')
def change_partners_status(request):
    if request.method == 'POST':
        partners_id = request.POST.get('partners_id')
        new_status = request.POST.get('new_status')
        partners = Company.objects.get(pk=partners_id)
        partners.status = new_status
        partners.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})