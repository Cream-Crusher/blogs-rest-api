from rest_framework import serializers
from application.models import User, Blog


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
    subscriptions = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all(), many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'is_admin', 'password', 'subscriptions']

    def create(self, validated_data):
        subscriptions_list = validated_data.pop('subscriptions', [])
        user = super().create(validated_data)

        if subscriptions_list:
            user.subscriptions.set(subscriptions_list)

        return user
