from application.models import Blog
from application.serializers.BlogSerializer import BlogSerializer


from rest_framework.response import Response
from rest_framework.views import APIView


class BlogsListView(APIView):
    def get(self, request):
        blogs = Blog.objects.order_by('updated_at').loading_db_queries()
        serializer = BlogSerializer(
            instance=blogs,
            many=True
        )
        return Response(serializer.data)
