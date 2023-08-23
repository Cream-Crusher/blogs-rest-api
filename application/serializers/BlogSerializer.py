from rest_framework import serializers, exceptions

from application.models import Blog, User, Post

from application.serializers.UserSerializer import UserSerializer
from application.serializers.PostSerializer import BlogPostSerializer


class BlogSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False)
    authors = UserSerializer(many=True)
    posts = BlogPostSerializer(many=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'owner', 'authors', 'posts']


class BlogCRUDSerializer(serializers.ModelSerializer):
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
        user = self.context['request'].user
        owner_id = instance.owner.id
        authors_id = [author.id for author in instance.authors.all()]

        if not (user.is_staff or user.id == owner_id):

            if user.id in authors_id:  # если пользователь есть в authors, то может редактировать посты.
                posts = validated_data.get('posts', instance.posts)
                instance.posts.set(posts)
                return instance
            else:
                raise exceptions.PermissionDenied("You are not allowed to perform this action.")

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()

        authors = validated_data.get('authors', instance.authors)
        posts = validated_data.get('posts', instance.posts)

        instance.authors.set(authors)
        instance.posts.set(posts)

        return instance
