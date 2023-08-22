from rest_framework import generics
from application.serializers.CommentSerializer import CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from application.models import Comment


class CommentList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetails(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
