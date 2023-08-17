from rest_framework import serializers
from application.models import Blog, User, Post

from application.serializers.UserSerializer import UserSerializer
from application.serializers.PostSerializer import PostModelSerializer


class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    owner = UserSerializer(many=False)
    authors = UserSerializer(many=True)
    posts = PostModelSerializer(many=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'owner', 'authors', 'posts']


class BlogSerializerСhanges(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=50)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField()

    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)
    authors = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    posts = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), many=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'owner', 'authors', 'posts']

    def create(self, validated_data):
        authors_list = validated_data.pop('authors', [])
        blog = super().create(validated_data)

        if authors_list:
            blog.authors.set(authors_list)

        return blog

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        authors = instance.authors.all()

        for author in authors:
            instance.authors.add(author)

        return instance
