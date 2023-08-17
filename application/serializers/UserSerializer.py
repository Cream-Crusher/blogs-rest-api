from rest_framework import serializers
from application.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    is_admin = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'is_admin']


class UserSerializerСhanges(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    is_admin = serializers.BooleanField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ['id', 'username', 'is_admin', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
