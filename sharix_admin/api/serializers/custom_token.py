from rest_framework import serializers


class CustomTokenSerializer(serializers.Serializer):
    user = serializers.IntegerField(source='user.pk')
    auth_token = serializers.CharField(source="key")

    class Meta:
        fields = ("user", "auth_token")
