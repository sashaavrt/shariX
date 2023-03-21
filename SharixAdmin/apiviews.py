#REST API ---------------------------
from .serializer import *
from rest_framework import viewsets, permissions, exceptions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from SharixAdmin.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from xmpp import cli

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
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def get(self, request, format=None):
        return Response({"message": "Для отправки сообщения используйте POST-запрос"})
    
    def post(self, request, format=None):
        cli.send_message("sender", "password", "getter", request.data)
        return Response({"message": "Сообщение успешно отправлено!"})