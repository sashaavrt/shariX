from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Shema views
@login_required
def schema_v3(request):
    return render(request, "sharix_admin/schema.html")
