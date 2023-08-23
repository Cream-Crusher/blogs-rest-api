from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from application.serializers.BlogSerializer import BlogSerializer, BlogCRUDSerializer

from application.models import Blog


class BlogsList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Blog.objects.loading_db_queries()
    serializer_class = BlogSerializer


class SubscriptionsBlog(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        blogs = Blog.objects.filter(subscription_blogs=request.user).loading_db_queries()

        serializer = BlogSerializer(
            instance=blogs,
            many=True
        )

        return Response(serializer.data)


class BlogDetails(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Blog.objects.loading_db_queries()
    serializer_class = BlogCRUDSerializer
