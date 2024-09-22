from rest_framework import serializers


class CustomTokenSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(source='user.pk')
    auth_token = serializers.CharField(source="key")

    class Meta:
        fields = ("user_id", "auth_token")