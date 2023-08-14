from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect

from application.serializers.PostSerializer import PostSerializer
from application.models import Post


class PostsListUserView(APIView):
    def get(self, request):
        try:
            posts = Post.objects.filter(author=request.user).count_like().loading_db_queries()
            serializer = PostSerializer(
                instance=posts,
                many=True
            )
            return Response(serializer.data)

        except TypeError:

            return redirect('/api/v1/drf-auth/login/?next=/api/posts/')
