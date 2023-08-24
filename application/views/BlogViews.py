from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend

from application.serializers.BlogSerializer import BlogSerializer, BlogCRUDSerializer

from application.models import Blog


class BlogsList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Blog.objects.loading_db_queries()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'owner', 'authors']


class SubscriptionsBlog(generics.ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'owner', 'authors']

    def get_queryset(self):
        user = self.request.user
        return Blog.objects.filter(subscription_blogs=user).loading_db_queries()


class BlogDetails(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Blog.objects.loading_db_queries()
    serializer_class = BlogCRUDSerializer
