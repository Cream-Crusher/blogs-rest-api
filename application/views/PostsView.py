from rest_framework.views import APIView
from rest_framework.response import Response

from application.serializers.PostSerializer import PostSerializer
from application.models import Post


class PostsListView(APIView):
    def get(self, request):
        posts = Post.objects.filter(is_published=True).count_like().loading_db_queries()
        serializer = PostSerializer(
            instance=posts,
            many=True
        )
        return Response(serializer.data)
