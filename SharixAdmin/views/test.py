from SharixAdmin.views.context import get_context
from django.shortcuts import render

def testPage(request):
    context = get_context(request, {
        'title':'Страница в разработке'
        })
    return render(request, "SharixAdmin/test.html", context)