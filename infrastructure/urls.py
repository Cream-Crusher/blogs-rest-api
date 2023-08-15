from django.contrib import admin
from django.urls import path, include
from application.views import BlogViews, PostViews

from django.conf import settings

from .yasg_url import urlpatterns as doc_url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('home', BlogViews.BlogsList.as_view()),
    path('blog_list', BlogViews.BlogsList.as_view()),
    path('post_list', PostViews.PostsList.as_view()),

    path('my_post', PostViews.MyPost.as_view()),
    path('subscriptions_blog', BlogViews.SubscriptionsBlog.as_view()),
]

urlpatterns += doc_url

if settings.DEBUG:
    urlpatterns = [
            path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
