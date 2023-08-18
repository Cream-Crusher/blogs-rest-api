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
        blogs = Blog.objects.filter(subscription_blogs=request.user).loading_db_queries()

        serializer = BlogSerializer(
            instance=blogs,
            many=True
        )

        return Response(serializer.data)


class BlogDetails(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.order_by('updated_at').loading_db_queries()
    serializer_class = BlogSerializerСhanges

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.title = request.data.get('title')
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
