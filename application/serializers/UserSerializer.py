from rest_framework import serializers
from application.models import User, Blog
from rest_framework.exceptions import PermissionDenied


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    subscriptions = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all(), many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'is_staff', 'subscriptions']


class UserSerializerCreate(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    subscriptions = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all(), many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'subscriptions']

    def create(self, validated_data):
        subscriptions_list = validated_data.pop('subscriptions', [])
        user = super().create(validated_data)

        if subscriptions_list:
            user.subscriptions.set(subscriptions_list)

        return user


class UserSerializerСhanges(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    is_staff = serializers.BooleanField()
    subscriptions = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all(), many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'is_staff', 'subscriptions']

    def update(self, instance, validated_data):
        user = self.context['request'].user
        user_id = instance.id

        if not (user.is_staff or user.id == user_id):
            raise PermissionDenied("You are not allowed to perform this action.")

        if user.is_staff:
            instance.is_staff = validated_data.get('is_staff', instance.is_staff)

        instance.username = validated_data.get('username', instance.username)

        instance.save()

        subscriptions = validated_data.get('subscriptions', instance.subscriptions)

        instance.subscriptions.set(subscriptions)

        return instance
