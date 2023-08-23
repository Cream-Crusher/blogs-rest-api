from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from application.serializers.PostSerializer import PostSerializer, PostCRUDSerializer

from application.models import Post

from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse


class PostsList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.filter(is_published=True).count_like().loading_db_queries()
    serializer_class = PostSerializer


class PostDetails(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.count_like().loading_db_queries()
    serializer_class = PostCRUDSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)

        return Response(serializer.data)


class MyPost(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = Post.objects.filter(author=request.user).count_like().loading_db_queries()
        serializer = PostSerializer(
            instance=posts,
            many=True
        )
        return Response(serializer.data)


def PostLike(request, pk):
    post = get_object_or_404(Post, id=pk)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect(reverse('post_id', args=[str(pk)]))
