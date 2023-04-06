from django.urls import path, include, re_path
from .views import *
from .apiviews import *
from rest_framework import routers
from django_spaghetti.views import Plate
from schema_graph.views import Schema
from django.contrib.auth.decorators import login_required

router = routers.SimpleRouter()
router.register(r'sharix-users', SharixUserMVS)
router.register(r'group', GroupMVS)

urlpatterns = [
    #path('auth/', LoginSharix.as_view(), name='auth'),
    path('accounts/login/', LoginSharix.as_view(), name='authweb'),
    path('', index, name='home'),
    path('transactions/', transactions, name='trans'),
    path('transactions/<int:trans_id>/', trans_id, name='transid'),
    path('logout/', logout_view, name='logoutweb'),
    path('balance/', balance, name='balance'),
    path('test/', testPage, name='test-page'),
    
    #path('v1/auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'), name='auth'),
    path('platform/api/', include(router.urls), name="sharix-api"),
    path('senderphone/', PhoneSender.as_view()),
    #schemas
    path('schemav1/', login_required(Schema.as_view()), name='schemav1'),
    path('schemav2/', login_required(Plate.as_view()),  name='schemav2'),
    path('schemav3/', schema_v3, name='schema'),
    
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]