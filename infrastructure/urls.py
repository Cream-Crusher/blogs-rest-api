from django.urls import path, include
from django.contrib import admin
from django.conf import settings

from application.views import BlogViews, PostViews, TagViews, UserViews, CommentViews

from .yasg_url import urlpatterns as doc_url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'), name='auth'),

    path('home', BlogViews.GetBlogsListDTO.as_view(), name='home'),

    path('blog/', BlogViews.GetBlogsListDTO.as_view(), name='blog'),
    path('blog/subscriptions', BlogViews.GetSubscriptionsBlogDTO.as_view(), name='blog_create'),
    path('blog/create', BlogViews.CreateBlogDTO.as_view(), name='blog_subscriptions'),
    path('blog/<int:pk>', BlogViews.GetBlogDTO.as_view(), name='blog_id'),

    path('post/', PostViews.GetPostsListDTO.as_view(), name='post'),
    path('post/my', PostViews.MyPostDTO.as_view(), name='my_post'),
    path('post/create', PostViews.CreatePostDTO.as_view(), name='post_create'),
    path('post/<int:pk>', PostViews.GetPostDTO.as_view(), name='post_id'),
    path('post/<int:pk>/like/', PostViews.PostLike, name="post_like"),

    path('tag/', TagViews.GetTagsListDTO.as_view()),
    path('tag/create', TagViews.CreateTagDTO.as_view()),
    path('tag/<int:pk>', TagViews.GetTagDTO.as_view()),

    path('user/', UserViews.GetUsersListDTO.as_view()),
    path('user/create', UserViews.CreateUserDTO.as_view()),
    path('user/<int:pk>', UserViews.GetUserDTO.as_view()),

    path('сomment/', CommentViews.GetCommentsListDTO.as_view()),
    path('сomment/create', CommentViews.CreateCommentDTO.as_view()),
    path('сomment/<int:pk>', CommentViews.GetCommentDTO.as_view()),
]

urlpatterns += doc_url

if settings.DEBUG:
    urlpatterns = [
            path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
