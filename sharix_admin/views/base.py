from django.views import View


class BaseView(View):
    """
    Базовый класс представления админ-панели ShariX.

    Предоставляет общие методы и функционал, который
    может быть использован в других представлениях админ-панели.
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'title': self.page_title,
            'current_page': self.page_name,
            'is_partner_admin': self.request.user.groups.filter(name='PARTNER-ADMIN').exists()
        })
        
        return context