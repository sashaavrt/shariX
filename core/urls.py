from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns



urlpatterns = (
    [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),

    ] + i18n_patterns(
        path('i18n/', include('django.conf.urls.i18n')),
        path('', include('SharixAdmin.urls')),
        path('tickets/', include("tickets.urls"), name='tickets'),
        path('design/', include("design_template.urls"), name='design'),
        #metaservice
        path('metaservicesynced/', include("metaservicesynced.urls"), name="metaservicesynced"),
        path('openlocal/', include("openlocal.urls"), name="openlocal"),
        prefix_default_language=False,
    )

    

    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  )

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)