from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_migrate


# Создание групп
@receiver(post_migrate)
def create_groups(sender, **kwargs):
    Group.objects.get_or_create(pk=21, name='METASERVICE-ADMIN')
    Group.objects.get_or_create(pk=22, name='METASERVICE-SUPERVISOR')
    Group.objects.get_or_create(pk=23, name='METASERVICE-SUPPORT')
    Group.objects.get_or_create(pk=24, name='METASERVICE-TECHSUPPORT')

    Group.objects.get_or_create(pk=31, name='PARTNER-ADMIN')
    Group.objects.get_or_create(pk=32, name='PARTNER-SUPERVISOR')
    Group.objects.get_or_create(pk=33, name='PARTNER-SUPPORT')
    Group.objects.get_or_create(pk=34, name='PARTNER-TECHSUPPORT')

    Group.objects.get_or_create(pk=41, name='PROVIDER')
    Group.objects.get_or_create(pk=51, name='CLIENT')
    Group.objects.get_or_create(pk=61, name='GUEST')


