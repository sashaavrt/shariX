from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import View


class BaseView(UserPassesTestMixin, View):
    """
    Базовый класс представления админ-панели ShariX.

    Предоставляет общие методы и функционал, который
    может быть использован в других представлениях админ-панели.
    """

    def dispatch(self, request, *args, **kwargs):
        self.user_groups = self.request.user.groups.values_list('name', flat=True)
        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        return True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'title': self.page_title,
            'current_page': self.page_name,
            'user_groups': self.user_groups
        })

        return context
