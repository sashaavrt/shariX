from django.contrib.auth import get_user_model

from django_tables2 import SingleTableView
from SharixAdmin.tables import UserInfoTable
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import Group
from django.utils.translation import gettext as _


class UserListView(UserPassesTestMixin, SingleTableView):
    table_class = UserInfoTable
    queryset = get_user_model().objects.all()
    template_name = 'SharixAdmin/user_information.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': _('User Management'),
            'object_list': context['object_list'],
            'groups': Group.objects.all()
        })
        return context
    
    def test_func(self) -> bool or None:
        group_names = ('PROVIDER')
        if bool(self.request.user.groups.filter(name=group_names)) or self.request.user.is_superuser:
            return True
        return False