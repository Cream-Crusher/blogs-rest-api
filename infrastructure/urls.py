from django.contrib import admin
from django.urls import path, include
from application.views import BlogViews, PostViews

from django.conf import settings

from .yasg_url import urlpatterns as doc_url


urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/v1/drf-auth/', include('rest_framework.urls')),
   path('api/home_page/', BlogViews.BlogsView.as_view()),

   path('api/blog/<int:id>', BlogViews.BlogView.as_view()),
   path('api/blogs/', BlogViews.BlogsView.as_view()),
   path('api/user_blogs/', BlogViews.UserBlogsView.as_view()),

   path('api/posts/', PostViews.PostsView.as_view()),
   path('api/user_posts/', PostViews.UserPostsView.as_view()),
]

urlpatterns += doc_url

if settings.DEBUG:
    urlpatterns = [
            path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
