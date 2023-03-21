from rest_framework import serializers
#from rest_framework.exceptions import ValidationError
#from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.models import *

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()
    group_name = serializers.ReadOnlyField(source="groups.name")
    class Meta:
        model = SharixUser
        exclude = ['password', 'id']
        read_only_fields = ['username', 'phone_number']
        extra_kwargs = {
            'first_name': {'write_only': True},
            'last_name':{'write_only':True}
        }
    def validate(self, attrs):
        return super().validate(attrs)

class GroupToUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupManager
        fields = "__all__"
    
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "name")