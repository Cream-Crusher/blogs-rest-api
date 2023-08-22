from rest_framework import serializers
from application.models import Blog, User, Post

from application.serializers.UserSerializer import UserSerializer
from application.serializers.PostSerializer import PostModelSerializer


class BlogSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False)
    authors = UserSerializer(many=True)
    posts = PostModelSerializer(many=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'owner', 'authors', 'posts']


class BlogSerializerСhanges(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
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
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        authors = validated_data.get('authors', instance.authors)
        posts = validated_data.get('posts', instance.posts)

        for author in authors:
            instance.authors.add(author)

        for post in posts:
            instance.posts.add(post)

        return instance
