from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#Shema views
@login_required
def schema_v3(request):
    return render(request, "SharixAdmin/schema.html")