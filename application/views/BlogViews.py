from rest_framework import generics
from application.serializers.BlogSerializer import BlogSerializer, BlogSerializerСhanges
from rest_framework.views import APIView
from rest_framework.response import Response

from application.models import Blog


class BlogsList(generics.ListAPIView):
    queryset = Blog.objects.order_by('updated_at').loading_db_queries()
    serializer_class = BlogSerializer


class SubscriptionsBlog(APIView):
    def get(self, request):
        blogs = Blog.objects.order_by('updated_at').filter(subscription_blogs=request.user).loading_db_queries()

        serializer = BlogSerializer(
            instance=blogs,
            many=True
        )

        return Response(serializer.data)


class BlogDetails(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.order_by('updated_at').loading_db_queries()
    serializer_class = BlogSerializerСhanges
