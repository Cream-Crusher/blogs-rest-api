from rest_framework import generics
from application.serializers.BlogSerializer import BlogSerializer, BlogSerializerInteraction
from rest_framework.views import APIView
from rest_framework.response import Response

from application.models import Blog, User


class BlogList(generics.ListAPIView):
    queryset = Blog.objects.order_by('updated_at').loading_db_queries()
    serializer_class = BlogSerializer


class BlogsList(generics.ListAPIView):
    queryset = Blog.objects.order_by('updated_at').loading_db_queries()
    serializer_class = BlogSerializer


class SubscriptionsBlog(APIView):
    def get(self, request):
        user = User.objects.filter(username=request.user).first()
        subscriptions = user.subscriptions.all().loading_db_queries()
        serializer = BlogSerializer(
            instance=subscriptions,
            many=True
        )

        return Response(serializer.data)


class BlogDetails(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.order_by('updated_at').loading_db_queries()
    serializer_class = BlogSerializerInteraction
