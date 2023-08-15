from rest_framework import serializers

from application.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_admin', 'subscriptions']
