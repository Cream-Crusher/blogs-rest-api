from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import generics

from application.serializers.PostSerializer import PostSerializer, PostCRUDSerializer

from application.models import Post

from django_filters.rest_framework import DjangoFilterBackend, DateFromToRangeFilter
from django_filters import FilterSet
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse


class PostFilter(FilterSet):
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Post
        fields = ['title', 'tags', 'author', 'created_at', ]


class PostsList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.filter(is_published=True).count_like().loading_db_queries()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter


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


class MyPost(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).count_like().loading_db_queries()


def PostLike(request, pk):
    post = get_object_or_404(Post, id=pk)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect(reverse('post_id', args=[str(pk)]))
