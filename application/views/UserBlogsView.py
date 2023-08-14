from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect

from application.serializers.BlogSerializer import BlogSerializer
from application.models import Blog


class BlogListUserView(APIView):
    def get(self, request):
        try:
            blogs = Blog.objects.filter(authors=request.user).order_by('created_at').loading_db_queries()
            serializer = BlogSerializer(
                instance=blogs,
                many=True
            )
            return Response(serializer.data)

        except TypeError:

            return redirect('/api/v1/drf-auth/login/?next=/api/posts/')
