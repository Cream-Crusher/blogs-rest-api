from django.contrib import admin
from django.urls import path, include
from application import views

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home_page/', views.show_home, name='home_page'),
    path('blog/', views.show_blog, name='blogs'),
    path('post/', views.show_post, name='posts'),
    path('user_post/', views.show_user_post, name='user_posts'),
    path('user_blog/', views.show_user_blog, name='user_blogs'),
]

if settings.DEBUG:
    urlpatterns = [
            path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
