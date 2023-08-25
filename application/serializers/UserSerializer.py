from rest_framework import serializers, exceptions

from application.models import User, Blog


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'is_staff']


class UserSerializerCreate(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    subscriptions = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all(), many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'subscriptions']

    def create(self, validated_data):
        subscriptions_list = validated_data.pop('subscriptions', [])
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        if subscriptions_list:
            user.subscriptions.set(subscriptions_list)

        return user


class UserSerializerRUD(serializers.ModelSerializer):
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
            raise exceptions.PermissionDenied("You are not allowed to perform this action.")

        if user.is_staff:
            instance.is_staff = validated_data.get('is_staff', instance.is_staff)

        instance.username = validated_data.get('username', instance.username)

        instance.save()

        subscriptions = validated_data.get('subscriptions', instance.subscriptions)

        instance.subscriptions.set(subscriptions)

        return instance
