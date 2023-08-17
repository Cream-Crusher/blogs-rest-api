from rest_framework import serializers
from application.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'body', 'created_at']
