import os
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from tickets.models import TicketList

User = get_user_model()


@receiver(post_migrate)
def create_initial_groups(sender, **kwargs):
    groups = [
        ('METASERVICE-ADMIN', 21),
        ('METASERVICE-SUPERVISOR', 22),
        ('METASERVICE-SUPPORT', 23),
        ('METASERVICE-TECHSUPPORT', 24),
        ('PARTNER-ADMIN', 31),
        ('PARTNER-SUPERVISOR', 32),
        ('PARTNER-SUPPORT', 33),
        ('PARTNER-TECHSUPPORT', 34),
        ('PROVIDER', 41),
        ('CLIENT', 51),
        ('GUEST', 61),
        ('TEST', 99)
    ]

    for name, pk in groups:
        group, created = Group.objects.get_or_create(name=name, defaults={'pk': pk})
        if not created:
            print(f"Group {name} already exists.")


@receiver(post_migrate)
def create_test_users(sender, **kwargs):
    """
    Создает тестовых пользователей, но только если установочный скрипт был запущен с параметром --test-users
    или была задана переменная окружения TEST_USERS=true.
    """
    if os.getenv('TEST_USERS') == 'true':
        password = make_password("sharix-open-test")
        test_group = Group.objects.get(pk=99)

        # Группа, в которой надо создать пользователя и их количество
        test_users = [
            ('METASERVICE-ADMIN', 1),
            ('METASERVICE-SUPERVISOR', 3),
            ('METASERVICE-SUPPORT', 3),
            ('METASERVICE-TECHSUPPORT', 3),

            ('PARTNER-ADMIN', 1),
            ('PARTNER-SUPERVISOR', 3),
            ('PARTNER-SUPPORT', 3),
            ('PARTNER-TECHSUPPORT', 3),

            ('PROVIDER', 3),
            ('CLIENT', 3),
            ('GUEST', 3)
        ]

        for test_user in test_users:
            group_name = test_user[0]
            group = Group.objects.get(name=group_name)

            for i in range(1, test_user[1] + 1):
                user, created = User.objects.get_or_create(
                    phone_number=f"{group.pk}0{i}",
                    defaults={
                        'last_name': i,
                        'first_name': group_name,
                        'email': f"test-{group_name.lower()}-{i}@domain.org",
                        'username': f"test-{group_name.lower()}-{i}",
                        'middle_name': "Test",
                        'password': password
                    }
                )

                if created:
                    user.groups.add(
                        test_group,
                        group
                    )
                    print(f"Test user created: {user}")


@receiver(post_migrate)
def create_initial_ticket_lists(sender, **kwargs):
    if sender.name == 'tickets':
        ticket_data = [
            # METASERVICE
            (2101, 'Активация партнеров (NEG_REQUEST)', 'METASERVICE-ADMIN'),
            (2102, 'Права в сервисе (ACCESS_REQUEST)', 'METASERVICE-ADMIN'),
            (2103, 'Проверка документов (ST_REQUEST)', 'METASERVICE-ADMIN'),
            (2201, 'Активность пользователей (ST_REQUEST)', 'METASERVICE-SUPERVISOR'),
            (2202, 'Оперативный доступ (ST_REQUEST)', 'METASERVICE-SUPERVISOR'),
            (2203, 'Оперативный доступ экстра (ACCESS_REQUEST)', 'METASERVICE-SUPERVISOR'),
            (2204, 'Права сервиса (ST_REQUEST)', 'METASERVICE-SUPERVISOR'),
            (2205, 'Проверка документов (ST_REQUEST)', 'METASERVICE-SUPERVISOR'),
            (2301, 'Входящие обычные заявки (ST_REQUEST)', 'METASERVICE-SUPPORT'),
            (2302, 'Заявки на услуги сервиса (SERVICE_REQUEST)', 'METASERVICE-SUPPORT'),
            (2401, 'Входящие технические заявки (ST_REQUEST)', 'METASERVICE-TECHSUPPORT'),
            # PARTNER
            (3101, 'Документы исполнителей (ST_REQUEST)', 'PARTNER-ADMIN'),
            (3102, 'Документы ресурсов (ST_REQUEST)', 'PARTNER-ADMIN'),
            (3103, 'Права в партнерке (ACCESS_REQUEST)', 'PARTNER-ADMIN'),
            (3201, 'Активность внутри партнера (ST_REQUEST)', 'PARTNER-SUPERVISOR'),
            (3202, 'Документы исполнителей (ST_REQUEST)', 'PARTNER-SUPERVISOR'),
            (3203, 'Документы ресурсов (ST_REQUEST)', 'PARTNER-SUPERVISOR'),
            (3204, 'Доступ внутри партнера (ST_REQUEST)', 'PARTNER-SUPERVISOR'),
            (3205, 'Оперативный доступ (ST_REQUEST)', 'PARTNER-SUPERVISOR'),
            (3206, 'Оперативный доступ экстра (ST_REQUEST)', 'PARTNER-SUPERVISOR'),
            (3207, 'Ручное подтверждение заявок (ACCESS-REQUEST)', 'PARTNER-SUPERVISOR'),
            (3401, 'Входящие технические заявки (ST_REQUEST)', 'PARTNER-TECHSUPPORT'),
        ]

        for pk, name, group_name in ticket_data:
            group = Group.objects.get(name=group_name)
            # Проверяем существование тикета с таким же name и group
            ticket_exists = TicketList.objects.filter(group=group, name=name).exists()

            if not ticket_exists:
                TicketList.objects.create(pk=pk, name=name, group=group)


# Откючаем тестовых пользователей (если такие есть), если DEBUG=False и наоброт
try:
    if Group.objects.filter(name="TEST").exists():
        test_group = Group.objects.get(name="TEST")
        users_in_test_group = User.objects.filter(groups=test_group)

        if users_in_test_group:
            users_in_test_group.update(is_active=settings.DEBUG)
except:
    print("Test user validation is not available. Models have not been created yet")
