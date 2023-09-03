from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('', include('SharixAdmin.urls')),
    path('tickets/', include('tickets.urls', namespace='tickets'), name='tickets'),
    path('metaservicesynced/', include("metaservicesynced.urls"), name="metaservicesynced"),
] 

if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
   urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))