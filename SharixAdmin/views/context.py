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
    {'title':'Исполнители',             'link':'provider', 'sel':'people'},
    {'title':'Тарифы услуг',            'link':'service_tariff', 'sel':'person'},
    {'title':'Партнеры',                'link':'partners', 'sel':'people'},
    {'title':'Ресурсы',                 'link':'resource', 'sel':'sotrud'},
    {'title':'Услуги сервиса',          'link':'service_type', 'sel':'hdd-network'},
    {'title':'Информация о сервисе',    'link':'partner_information/add/', 'sel':'hdd-network'},
    {'title':'Информация о партнере',   'link':'partner_information/add/', 'sel':'person'},
    {'title':'Тарифы',                  'link':'service', 'sel':'tikets'},
]

def get_context(request, page_context) -> dict:
    base_context = {
        "title":page_context['title'],
        'url_path':resolve(request.path_info).url_name,
        'menu':menu
    }
    context = dict(list(base_context.items()) + list(page_context.items()))
    return context