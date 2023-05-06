from django.urls import resolve

menu = [
    {'title':'Главная/баланс',          'link':'home', 'sel':'house'},
    {'title':'Платежная информация',    'link':'test-page', 'sel':'credit-card'},
    {'title':'История платежей',        'link':'trans','sel':'clock-history'},
    {'title':'Курсы',                   'link':'course', 'sel':'education'},
    {'title':'Личная информация',       'link':'test-page', 'sel':'person'},
    {'title':'Управление сервисами',    'link':'test-page', 'sel':'hdd-network'},
    {'title':'Мои связи',               'link':'test-page', 'sel':'people'},
    {'title':'Сотрудничество',          'link':'test-page', 'sel':'sotrud'},
    {'title':'Техподдержка',            'link':'test-page', 'sel':'gear'},
    {'title':'Мои заявки',              'link':'tickets', 'sel':'tikets'},
    {'title':'Исполнители',             'link':'provider', 'sel':'people', 
     'roles':['METASERVICE-ADMIN']},
    {'title':'Тарифы услуг',            'link':'service_tariff', 'sel':'person',
     'roles':['PARTNER-ADMIN']},
    {'title':'Партнеры',                'link':'partners', 'sel':'people',
     'roles':['METASERVICE-ADMIN']},
    {'title':'Ресурсы',                 'link':'resource', 'sel':'sotrud',
     'roles':['PARTNER-ADMIN']},
    {'title':'Услуги сервиса',          'link':'service_type', 'sel':'hdd-network',
     'roles':['METASERVICE-ADMIN']},
    {'title':'Информация о сервисе',    'link':'service_information/add/', 'sel':'hdd-network',
     'roles':['METASERVICE-ADMIN']},
    {'title':'Информация о партнере',   'link':'partner_information/add/', 'sel':'person',
     'roles':['PARTNER-ADMIN']},
    {'title':'Тарифы',                  'link':'service', 'sel':'tikets'},
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