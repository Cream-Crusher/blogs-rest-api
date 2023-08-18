from django.contrib import admin
from django.urls import path, include
from application.views import BlogViews, PostViews, TagViews, UserViews, CommentViews

from django.conf import settings

from .yasg_url import urlpatterns as doc_url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('home', BlogViews.BlogsList.as_view()),

    path('blog/', BlogViews.BlogsList.as_view()),
    path('blog/subscriptions', BlogViews.SubscriptionsBlog.as_view()),
    path('blog/<int:pk>', BlogViews.BlogDetails.as_view()),

    path('post/', PostViews.PostsList.as_view(), name='post_home'),
    path('post/my', PostViews.MyPost.as_view()),
    path('post/<int:pk>', PostViews.PostDetails.as_view(), name='post_id'),
    path('post/<int:pk>/like/', PostViews.PostLike, name="post_like"),

    path('tag/', TagViews.TagList.as_view()),
    path('tag/<int:pk>', TagViews.TagDetails.as_view()),

    path('user/', UserViews.UserList.as_view()),
    path('user/<int:pk>', UserViews.UserDetails.as_view()),

    path('сomment/', CommentViews.CommentList.as_view()),
    path('сomment/<int:pk>', CommentViews.CommentDetails.as_view()),
]

urlpatterns += doc_url

if settings.DEBUG:
    urlpatterns = [
            path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
