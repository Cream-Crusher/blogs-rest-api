from rest_framework import serializers

from application.serializers.UserSerializer import UserSerializer


class BlogSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=50)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    owner = UserSerializer(read_only=True, many=False)
    authors = UserSerializer(read_only=True, many=True)
