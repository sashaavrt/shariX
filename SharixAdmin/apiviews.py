#REST API ---------------------------
from .serializer import *
from rest_framework import viewsets, permissions, exceptions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from SharixAdmin.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from xmpp import cli
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

schema_view = get_schema_view(
   openapi.Info(
      title="ShariX Admin Open API",
      default_version='v1',
      description="REST API Documentation",
      #terms_of_service="https://www.google.com/policies/terms/",
      #contact=openapi.Contact(email="contact@snippets.local"),
      #license=openapi.License(name="BSD License"),
   ),
   public=False,
   permission_classes=[permissions.IsAuthenticated],
)

class SharixUserMVS(viewsets.ModelViewSet):
    queryset = SharixUser.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsOwnerOrReadOnly]
    permission_classes = [permissions.IsAuthenticated]


class GroupMVS(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        #print(self.request.user.pk)
        return super().update(request, *args, **kwargs)
        
    #def get_queryset(self):
        #owner_req = self.queryset.filter(wallet=self.request.user.pk)
        #return owner_req    

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    
class PhoneSender(APIView):
    """
    Test description one
    """
    
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    
    @swagger_auto_schema(operation_description="Test description two")
    def get(self, request, format=None):
        return Response({"message": "Для отправки сообщения используйте POST-запрос"})
    
    @swagger_auto_schema(operation_description="Test description three")
    def post(self, request, format=None):
        cli.send_message("sender", "password", "getter", request.data)
        return Response({"message": "Сообщение успешно отправлено!"})