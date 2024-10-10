from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_migrate

from tickets.models import TicketList


@receiver(post_migrate)
def create_initial_groups(sender, **kwargs):
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


@receiver(post_migrate)
def create_initial_ticket_lists(sender, **kwargs):
    if sender.name == 'tickets':
        # METASERVICE
        ## ADMIN
        TicketList.objects.get_or_create(pk=2101, name='Активация партнеров (NEG_REQUEST)', group=Group.objects.get(name='METASERVICE-ADMIN'))
        TicketList.objects.get_or_create(pk=2102, name='Права в сервисе (ACCESS_REQUEST)', group=Group.objects.get(name='METASERVICE-ADMIN'))
        TicketList.objects.get_or_create(pk=2103, name='Проверка документов (ST_REQUEST)', group=Group.objects.get(name='METASERVICE-ADMIN'))

        ## SUPERVISOR
        TicketList.objects.get_or_create(pk=2201, name='Активность пользователей (ST_REQUEST)', group=Group.objects.get(name='METASERVICE-SUPERVISOR'))
        TicketList.objects.get_or_create(pk=2202, name='Оперативный доступ (ST_REQUEST)', group=Group.objects.get(name='METASERVICE-SUPERVISOR'))
        TicketList.objects.get_or_create(pk=2203, name='Оперативный доступ экстра (ACCESS_REQUEST)', group=Group.objects.get(name='METASERVICE-SUPERVISOR'))
        TicketList.objects.get_or_create(pk=2204, name='Права сервиса (ST_REQUEST)', group=Group.objects.get(name='METASERVICE-SUPERVISOR'))
        TicketList.objects.get_or_create(pk=2205, name='Проверка документов (ST_REQUEST)', group=Group.objects.get(name='METASERVICE-SUPERVISOR'))

        ## SUPPORT
        TicketList.objects.get_or_create(pk=2301, name='Входящие обычные заявки (ST_REQUEST)', group=Group.objects.get(name='METASERVICE-SUPPORT'))
        TicketList.objects.get_or_create(pk=2302, name='Заявки на услуги сервиса (SERVICE_REQUEST)', group=Group.objects.get(name='METASERVICE-SUPPORT'))

        ## TECHSUPPORT
        TicketList.objects.get_or_create(pk=2401, name='Входящие технические заявки (ST_REQUEST)', group=Group.objects.get(name='METASERVICE-TECHSUPPORT'))

        # PARTNER
        ## ADMIN
        TicketList.objects.get_or_create(pk=3101, name='Документы исполнителей (ST_REQUEST)', group=Group.objects.get(name='PARTNER-ADMIN'))
        TicketList.objects.get_or_create(pk=3102, name='Документы ресурсов (ST_REQUEST)', group=Group.objects.get(name='PARTNER-ADMIN'))
        TicketList.objects.get_or_create(pk=3103, name='Права в партнерке (ACCESS_REQUEST)', group=Group.objects.get(name='PARTNER-ADMIN'))
        
        ## SUPERVISOR
        TicketList.objects.get_or_create(pk=3201, name='Активность внутри партнера (ST_REQUEST)', group=Group.objects.get(name='PARTNER-SUPERVISOR'))
        TicketList.objects.get_or_create(pk=3202, name='Документы исполнителей (ST_REQUEST)', group=Group.objects.get(name='PARTNER-SUPERVISOR'))
        TicketList.objects.get_or_create(pk=3203, name='Документы ресурсов (ST_REQUEST)', group=Group.objects.get(name='PARTNER-SUPERVISOR'))
        TicketList.objects.get_or_create(pk=3204, name='Доступ внутри партнера (ST_REQUEST)', group=Group.objects.get(name='PARTNER-SUPERVISOR'))
        TicketList.objects.get_or_create(pk=3205, name='Оперативный доступ (ST_REQUEST)', group=Group.objects.get(name='PARTNER-SUPERVISOR'))
        TicketList.objects.get_or_create(pk=3206, name='Оперативный доступ экстра (ST_REQUEST)', group=Group.objects.get(name='PARTNER-SUPERVISOR'))
        TicketList.objects.get_or_create(pk=3207, name='Ручное подтверждение заявок (ACCESS-REQUEST)', group=Group.objects.get(name='PARTNER-SUPERVISOR'))
        
        ## TECHSUPPORT
        TicketList.objects.get_or_create(pk=3401, name='Входящие технические заявки (ST_REQUEST)', group=Group.objects.get(name='PARTNER-TECHSUPPORT'))