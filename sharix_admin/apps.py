from django.apps import AppConfig


class ShariXAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sharix_admin'
    verbose_name = "ShariX Open"

    def ready(self):
       import sharix_admin.signals