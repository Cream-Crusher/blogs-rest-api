from rest_framework import generics
from application.serializers.PostSerializer import PostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from application.models import Post


class PostsList(generics.ListAPIView):
    queryset = Post.objects.filter(is_published=True).count_like().loading_db_queries()
    serializer_class = PostSerializer


# class PostDetails(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
#     queryset = Post.objects.count_like().loading_db_queries()
#     serializer_class = PostSerializer


class MyPost(APIView):
    def get(self, request):
        posts = Post.objects.filter(author=request.user).count_like().loading_db_queries()
        serializer = PostSerializer(
            instance=posts,
            many=True
        )
        return Response(serializer.data)
