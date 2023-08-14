from application.models import Blog
from application.serializers.BlogSerializer import BlogSerializer


from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect, get_object_or_404


class BlogView(APIView):
    def get(self, request, id):
        blogs = get_object_or_404(Blog, id=id)
        serializer = BlogSerializer(
            instance=blogs,
        )
        return Response(serializer.data)


class BlogsView(APIView):
    def get(self, request):
        blogs = Blog.objects.order_by('updated_at').loading_db_queries()
        serializer = BlogSerializer(
            instance=blogs,
            many=True
        )
        return Response(serializer.data)


class UserBlogsView(APIView):
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
