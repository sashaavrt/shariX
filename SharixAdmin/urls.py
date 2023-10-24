from django.urls import path, include, re_path
from SharixAdmin.views import *
from .apiviews import *
from rest_framework import routers
from django_spaghetti.views import Plate
from schema_graph.views import Schema
from django.conf import settings
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
   
    path('partners/', login_required(PartnersListView.as_view()), name='partners'),
    path('partners/change_status/', change_partners_status, name='partners/change_status'),

    path('resource/', login_required(ResourceListView.as_view()), name='resource'),
    path('resource/change_status/', change_resource_status, name='resource/change_status'),
    
    path('provider/', login_required(ProviderListView.as_view()), name='provider'),
    path('provider/change_status/', change_provider_status, name='provider/change_status'),

    path('service_tariff/', login_required(ServiceTariffListView.as_view()), name='service_tariff'),
    path('service_tariff/add/', login_required(ServiceTariffCreate.as_view()), name='service_tariff/add/'),
    path('service_tariff/edit/<int:pk>', login_required(ServiceTariffUpdateView.as_view()), name='service_tariff/edit/'),

    path('service_type/', login_required(ServiceTypeListView.as_view()), name='service_type'),
    path('service_type/edit/<int:pk>', login_required(ServiceTypeUpdateView.as_view()), name='service_type/edit/'),
    path('service_type/add/', login_required(ServiceTypeCreate.as_view()), name='service_type/add/'),
    path('service_type/delete/<int:pk>', login_required(ServiceTypeDelete.as_view()), name='service_type/delete/'),

    path('service_information/add/', login_required(ServiceInformationCreate.as_view()), name='service_information/add/'),
    path('service_information/edit/<int:pk>', login_required(ServiceInformationUpdateView.as_view()), name='service_information/edit/'),
    
    path('service/', ServiceListView.as_view(), name='service'),
    path('service/change_status/', change_service_status, name='service/change_status'),

    path('partner_information/', login_required(PartnerInfoView.as_view()), name='partner_information/'),    
    path('partner_information/add/', login_required(PartnerInformationCreate.as_view()), name='partner_information/add/'),
    path('partner_information/edit/<int:pk>', login_required(PartnerInformationUpdateView.as_view()), name='partner_information/edit/'),

    path('user_information', login_required(UserListView.as_view()), name='user_information'),

    path('base/auth/', include('djoser.urls.authtoken'), name="api-auth"),
    path('base/', include(router.urls), name="api-base"),

    path('senderphone/', PhoneSender.as_view()),

    #schemas
    path('schemav1/', login_required(Schema.as_view()), name='schemav1'),
    path('schemav2/', login_required(Plate.as_view()),  name='schemav2'),
    path('schemav3/', schema_v3, name='schema'),
    
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
