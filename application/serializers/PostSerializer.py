from rest_framework import serializers

from application.serializers.UserSerializer import UserSerializer
from application.serializers.TagSerializer import TagSerializer


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    body = serializers.CharField()
    is_published = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    views = serializers.IntegerField()

    author = UserSerializer(read_only=True, many=False)
    tags = TagSerializer(read_only=True, many=True)

    like_count = serializers.IntegerField()
