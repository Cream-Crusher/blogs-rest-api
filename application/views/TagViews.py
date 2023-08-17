from rest_framework import generics
from application.serializers.TagSerializer import TagSerializer

from application.models import Tag


class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetails(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
