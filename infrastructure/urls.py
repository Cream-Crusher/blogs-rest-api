from django.urls import path, include
from django.contrib import admin
from django.conf import settings

from application.views import BlogViews, PostViews, TagViews, UserViews, CommentViews

from .yasg_url import urlpatterns as doc_url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'), name='auth'),

    path('home', BlogViews.BlogsList.as_view(), name='home'),

    path('blog/', BlogViews.BlogsList.as_view(), name='blog'),
    path('blog/subscriptions', BlogViews.SubscriptionsBlog.as_view(), name='blog_subscriptions'),
    path('blog/<int:pk>', BlogViews.BlogDetails.as_view(), name='blog_id'),

    path('post/', PostViews.PostsList.as_view(), name='post'),
    path('post/my', PostViews.MyPost.as_view(), name='my_post'),
    path('post/<int:pk>', PostViews.PostDetails.as_view(), name='post_id'),
    path('post/<int:pk>/like/', PostViews.PostLike, name="post_like"),

    path('tag/', TagViews.TagList.as_view()),
    path('tag/<int:pk>', TagViews.TagDetails.as_view()),

    path('user/', UserViews.UserList.as_view()),
    path('user/<int:pk>', UserViews.UserCreate.as_view()),
    path('user/<int:pk>/update', UserViews.UserDetails.as_view()),

    path('сomment/', CommentViews.CommentList.as_view()),
    path('сomment/<int:pk>', CommentViews.CommentDetails.as_view()),
]

urlpatterns += doc_url

if settings.DEBUG:
    urlpatterns = [
            path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
