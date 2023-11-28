from django.urls import resolve
from django.utils.translation import gettext_lazy as _

menu = [
    {'title':_('Главная'),          'link':'home', 'sel':'house'},
    {'title':_('Заявки'),              'link':'tickets', 'sel':'tikets'},
    {'title':_('Партнеры'),                'link':'partners', 'sel':'people',
     'roles':['METASERVICE-ADMIN']},
    {'title':_('Управление правами'),'link':'user_information', 'sel':'person'},
    {'title':_('Услуги сервиса'),          'link':'service_type', 'sel':'hdd-network',
     'roles':['METASERVICE-ADMIN']},
    {'title':_('История заказов'),        'link':'trans','sel':'clock-history'},
    {'title':_('Информация о сервисе'),    'link':'service_information/add/', 'sel':'hdd-network',
     'roles':['METASERVICE-ADMIN']},
    {'title':_('Оплата'),    'link':'test-page', 'sel':'credit-card'},

]

def get_context(request, page_context) -> dict:
    # Получаем роли текущего пользователя
    user_roles = set(group.name for group in request.user.groups.all())
    is_superuser = request.user.is_superuser
    menu_items = []
    # Добавляем только те страницы к которым должен быть доступ
    for item in menu:
        if not item.get('roles') or is_superuser or set(item['roles']) & set(user_roles):  
            menu_items.append(item)

    base_context = {
        "title":page_context['title'],
        'url_path':resolve(request.path_info).url_name,
        'menu':menu_items
    }
    context = dict(list(base_context.items()) + list(page_context.items()))
    return context