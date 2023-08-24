from rest_framework import serializers, exceptions

from application.serializers.CommentSerializer import CommentSerializer
from application.serializers.UserSerializer import UserSerializer
from application.serializers.TagSerializer import TagSerializer
from application.models import Post, Tag, User


class BlogPostSerializer(serializers.ModelSerializer):  # Запросы данных для других сериализаторов

    class Meta:
        fields = '__all__'
        model = Post


class PostSerializer(serializers.ModelSerializer):  # Запросы получения данных
    author = UserSerializer(many=False)
    tags = TagSerializer(many=True)
    comments = CommentSerializer(many=True)

    like_count = serializers.IntegerField()
    relevance = serializers.IntegerField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'is_published', 'created_at', 'views', 'author', 'tags', 'like_count', 'comments', 'relevance']


class PostCRUDSerializer(serializers.ModelSerializer):  # запросы изменеия данных
    id = serializers.IntegerField(read_only=True)
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
        user = self.context['request'].user
        author_id = instance.author.id

        if not (user.is_staff or user.id == author_id):
            raise exceptions.PermissionDenied("You are not allowed to perform this action.")

        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.views = validated_data.get('views', instance.views)
        instance.author = validated_data.get('author', instance.author)
        instance.save()

        tags = validated_data.get('tags', instance.views)

        instance.tags.set(tags)

        return instance
