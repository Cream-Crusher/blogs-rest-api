# url
from django.contrib import admin
from django.urls import path, include, re_path
from application import views

# swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Настройки
from django.conf import settings


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
   #  path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   #  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   #  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('home_page/', views.show_home, name='home_page'),
    path('blog/', views.show_blog, name='blogs'),
    path('post/', views.show_post, name='posts'),
    path('user_post/', views.show_user_post, name='user_posts'),
    path('user_blog/', views.show_user_blog, name='user_blogs'),
    path('accounts/', include('django.contrib.auth.urls'))
]

if settings.DEBUG:
    urlpatterns = [
            path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
