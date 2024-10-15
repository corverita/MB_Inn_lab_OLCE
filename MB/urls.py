"""
URL configuration for MB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls.conf import include
from django.conf import settings

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API MB Lab",
        default_version='v1',
        description="API del sistema MB Innovation Lab",
        contact=openapi.Contact(email="oscar.corvera@live.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/v1/', include('apps.users.urls')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # Registra el nombre de espacio 'rest_framework' para las rutas de autenticación
]

if settings.DEBUG:
    urlpatterns += [
        path('admin/', admin.site.urls),
        # Path API Swagger
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
        path('swagger/api/v1/user/login/', schema_view.with_ui('swagger', cache_timeout=0), name='rest_framework_login'),
        path('swagger/api/v1/user/logout/', schema_view.with_ui('swagger', cache_timeout=0), name='rest_framework_logout'),
    ]