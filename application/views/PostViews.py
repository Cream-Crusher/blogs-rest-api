from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework import generics

from application.serializers.PostSerializer import PostSerializer, PostCRUDSerializer
from application.models import Post

from django_filters.rest_framework import DjangoFilterBackend, DateFromToRangeFilter, NumberFilter
from django_filters import FilterSet, CharFilter
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse


class PostFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    tags = CharFilter(field_name='tags', lookup_expr='icontains')
    author = CharFilter(field_name='author', lookup_expr='icontains')
    created_at = DateFromToRangeFilter(field_name='created_at', lookup_expr='gte')
    like_count = NumberFilter(field_name='like_count', lookup_expr='gte')
    relevance = NumberFilter(field_name='relevance', lookup_expr='gte')

    class Meta:
        model = Post
        fields = ['title', 'tags', 'author', 'created_at', 'like_count', 'relevance']


class PostsList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.filter(is_published=True).count_like().loading_db_queries().calculate_relevance()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = PostFilter
    ordering_fields = ['title', 'tags', 'author', 'created_at', 'like_count', 'relevance']


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
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = PostFilter
    ordering_fields = ['title', 'tags', 'author', 'created_at', 'like_count']

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).count_like().loading_db_queries()


def PostLike(request, pk):
    post = get_object_or_404(Post, id=pk)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect(reverse('post_id', args=[str(pk)]))
