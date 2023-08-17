from rest_framework import generics
from application.serializers.CommentSerializer import CommentSerializer

from application.models import Comment


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetails(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
