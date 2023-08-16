from rest_framework import serializers
from application.models import Blog

from application.serializers.UserSerializer import UserSerializer


class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=50)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    owner = UserSerializer(many=False)
    authors = UserSerializer(many=True)

    def create(self, validated_data):
        return Blog(**validated_data)

    def update(self, instance, validated_data): 
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        authors = instance.authors.all()

        authors = instance.authors.all()

        for author in authors:
            instance.authors.add(author)

        return instance
