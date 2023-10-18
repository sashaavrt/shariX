from django.urls import resolve
from django.utils.translation import gettext_lazy as _

menu = [
    {'title':_('Home/Balance'),          'link':'home', 'sel':'house'},
    {'title':_('Payment information'),    'link':'test-page', 'sel':'credit-card'},
    {'title':_('Payment history'),        'link':'trans','sel':'clock-history'},
    {'title':_('Courses'),                   'link':'course', 'sel':'education'},
    {'title':_('Personal information'),       'link':'test-page', 'sel':'person'},
    {'title':_('Service management'),    'link':'test-page', 'sel':'hdd-network'},
    {'title':_('My connections'),               'link':'test-page', 'sel':'people'},
    {'title':_('Partnership'),          'link':'test-page', 'sel':'sotrud'},
    {'title':_('Techsupport'),            'link':'test-page', 'sel':'gear'},
    {'title':_('My tickets'),              'link':'tickets', 'sel':'tikets'},
    {'title':_('Performers'),             'link':'provider', 'sel':'people', 
     'roles':['METASERVICE-ADMIN']},
    {'title':_('Service rates'),            'link':'service_tariff', 'sel':'person',
     'roles':['PARTNER-ADMIN']},
    {'title':_('Partners'),                'link':'partners', 'sel':'people',
     'roles':['METASERVICE-ADMIN']},
    {'title':_('Resources'),                 'link':'resource', 'sel':'sotrud',
     'roles':['PARTNER-ADMIN']},
    {'title':_('Service services'),          'link':'service_type', 'sel':'hdd-network',
     'roles':['METASERVICE-ADMIN']},
    {'title':_('Information about the service'),    'link':'service_information/add/', 'sel':'hdd-network',
     'roles':['METASERVICE-ADMIN']},
    {'title':_('Partner Information'),   'link':'partner_information/', 'sel':'person',
     'roles':['PARTNER-ADMIN']},
    {'title':_('Rates'),                  'link':'service', 'sel':'tikets',
     'roles':['PARTNER-ADMIN']},
    {'title':_('User Management'),'link':'user_information', 'sel':'person'}
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