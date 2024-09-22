from django.apps import AppConfig


class ShariXAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sharix_admin'
    verbose_name = "SHARIX_OPEN"

    def ready(self):
       import sharix_admin.signals