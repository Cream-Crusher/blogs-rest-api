from rest_framework import serializers
from application.models import Post, Tag, User

from application.serializers.UserSerializer import UserSerializer
from application.serializers.TagSerializer import TagSerializer
from application.serializers.CommentSerializer import CommentSerializer


class PostModelSerializer(serializers.ModelSerializer):  # Запросы данных для других сериализаторов
    id = serializers.IntegerField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class PostSerializer(serializers.Serializer):  # Запросы получения данных
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    body = serializers.CharField()
    is_published = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    views = serializers.IntegerField()

    author = UserSerializer(many=False)
    tags = TagSerializer(many=True)

    like_count = serializers.IntegerField()
    comments = CommentSerializer(many=True)


class PostSerializerСhanges(serializers.ModelSerializer):  # запросы изменеия данных
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    body = serializers.CharField()
    is_published = serializers.BooleanField()
    views = serializers.IntegerField(read_only=True)

    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    like_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'is_published', 'views', 'author', 'tags', 'like_count']

    def create(self, validated_data):
        tags_list = validated_data.pop('tags', [])
        post = super().create(validated_data)

        if tags_list:
            post.tags.set(tags_list)

        return post

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.views = validated_data.get('views', instance.views)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        tags = validated_data.get('tags', instance.views)

        for tag in tags:
            instance.tags.add(tag)

        return instance
