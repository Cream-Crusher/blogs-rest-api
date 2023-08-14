from django.contrib import admin
from django.urls import path, include
from application.views import BlogsView, PostsView, UserPostsView, UserBlogsView

from django.conf import settings

from .yasg_url import urlpatterns as doc_url


urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/v1/drf-auth/', include('rest_framework.urls')),
   path('api/home_page/', BlogsView.BlogsListView.as_view()),
   path('api/blogs/', BlogsView.BlogsListView.as_view()),
   path('api/posts/', PostsView.PostsListView.as_view()),
   path('api/user_posts/', UserPostsView.PostsListUserView.as_view()),
   path('api/user_blogs/', UserBlogsView.BlogListUserView.as_view()),
]

urlpatterns += doc_url

if settings.DEBUG:
    urlpatterns = [
            path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
