from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework import generics

from application.serializers.CommentSerializer import CommentSerializer
from application.models import Comment


class GetCommentsListDTO(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CreateCommentDTO(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class GetCommentDTO(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
