from rest_framework import serializers
from application.models import Post, Tag

from application.serializers.UserSerializer import UserSerializer
from application.serializers.TagSerializer import TagSerializer


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    body = serializers.CharField()
    is_published = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    views = serializers.IntegerField()

    author = UserSerializer(many=False)
    tags = TagSerializer(many=True)

    like_count = serializers.IntegerField()


class PostSerializerInteraction(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    body = serializers.CharField()
    is_published = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    views = serializers.IntegerField(read_only=True)

    author = UserSerializer(many=False)
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    like_count = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Post(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.views = validated_data.get('views', instance.views)
        instance.author = validated_data.get('author', instance.author)

        tags = instance.tag.all()

        for tag in tags:
            instance.tag.add(tag)

        return instance
