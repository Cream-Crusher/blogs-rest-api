from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.filters import OrderingFilter
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend, DateFromToRangeFilter
from django_filters import FilterSet


from application.serializers.BlogSerializer import BlogSerializer, BlogCRUDSerializer
from application.models import Blog


class BlogFilter(FilterSet):
    created_at = DateFromToRangeFilter()
    updated_at = DateFromToRangeFilter()

    class Meta:
        model = Blog
        fields = ['title', 'owner', 'authors', 'created_at', 'updated_at']


class BlogsList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Blog.objects.loading_db_queries()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = BlogFilter
    ordering_fields = ['title', 'owner', 'authors', 'created_at', 'updated_at']


class SubscriptionsBlog(generics.ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BlogFilter

    def get_queryset(self):
        user = self.request.user
        return Blog.objects.filter(subscription_blogs=user).loading_db_queries()


class BlogCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Blog.objects.loading_db_queries()
    serializer_class = BlogCRUDSerializer


class BlogDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Blog.objects.loading_db_queries()
    serializer_class = BlogCRUDSerializer
