from django.apps import AppConfig



class SharixadminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SharixAdmin'
    verbose_name = "SHARIX_PLATFORM"

    def ready(self):
        # Импортируем обработчик сигнала, чтобы зарегистрировать его
        from django.db.models.signals import post_migrate
        from .groups import create_groups
        post_migrate.connect(create_groups, sender=self)