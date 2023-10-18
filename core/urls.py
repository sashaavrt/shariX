from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
] + i18n_patterns(
        path('i18n/', include('django.conf.urls.i18n')),
        path('', include('SharixAdmin.urls')),
        path('tickets/', include('tickets.urls', namespace='tickets'), name='tickets'),
        path('design/', include("design_template.urls"), name='design'),
        path('metaservicesynced/', include("metaservicesynced.urls"), name="metaservicesynced"),
        path('webservice/', include("webservice_running.urls"), name='webservice_running'),
        path('landing/', include("landing.urls"), name="landing"),
        prefix_default_language=False,
    )
    

if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
   urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))