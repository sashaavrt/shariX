from django.apps import AppConfig



class SharixadminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SharixAdmin'
    verbose_name = "SHARIX_OPEN"

    def ready(self):
       import SharixAdmin.signals