from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_migrate
from django.contrib.auth.decorators import user_passes_test

#Создание групп
@receiver(post_migrate)
def create_groups(sender, **kwargs):
    Group.objects.get_or_create(pk=11, name='METASERVICE-ADMIN')
    Group.objects.get_or_create(pk=12, name='METASERVICE-SUPERVISOR')
    Group.objects.get_or_create(pk=13, name='METASERVICE-SUPPORT')
    Group.objects.get_or_create(pk=14, name='METASERVICE-TECHSUPPORT')
    Group.objects.get_or_create(pk=21, name='PARTNER-ADMIN')
    Group.objects.get_or_create(pk=22, name='PARTNER-SUPERVISOR')
    Group.objects.get_or_create(pk=23, name='PARTNER-SUPPORT')
    Group.objects.get_or_create(pk=24, name='PARTNER-TECHSUPPORT')
    Group.objects.get_or_create(pk=31, name='PROVIDER')
    Group.objects.get_or_create(pk=41, name='CLIENT')
    Group.objects.get_or_create(pk=51, name='GUEST')
    


# Функция позволяющая определить принадлежность к группе, перенаправляет на авторизацию
def group_required(*group_names):
    def in_groups(u):
        if u.is_authenticated:
            if u.groups.filter(name=group_names).exists() or u.is_superuser:
                return True
        return False

    return user_passes_test(in_groups)