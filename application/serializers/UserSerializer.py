from rest_framework import serializers

from application.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = User
        fields = ['id', 'username', 'is_admin', 'subscriptions']
