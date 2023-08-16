from rest_framework import serializers

from application.models import Tag


class TagSerializer(serializers.PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag_name']
