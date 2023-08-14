from rest_framework.views import APIView
from rest_framework.response import Response

from application.serializers.BlogSerializer import BlogSerializer
from application.models import Blog


class BlogView(APIView):
    def get(self, request):
        blogs = Blog.objects.get(request.id).loading_db_queries()
        serializer = BlogSerializer(
            instance=blogs,
        )
        return Response(serializer.data)
