from rest_framework import generics
from application.serializers.TagSerializer import TagSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

from application.models import Tag


class TagList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetails(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
