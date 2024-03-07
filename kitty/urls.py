"""
URL configuration for kitty project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import get_csrf_token
from users.api.router import router_user
from Carousel.api.router import router_carousel
from cats.api.router import router_cats,router_photoscats
from Asociations.api.router import router_asociations
from contactCard.api.router import router_contactCard
from webprofile.api.router import router_webprofile
from exhibitions.api.router import router_exhibition,router_photosexhibition
schema_view = get_schema_view(
   openapi.Info(
      title="Kitty API",
      default_version='v1',
      description="Back-end of my kitty website",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="javierexmar@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
  )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/',include('users.api.router')),
    path('api/',include(router_user.urls)),
    path('api/',include(router_carousel.urls)),
    path('api/',include(router_cats.urls)),
    path('api/',include(router_photoscats.urls)),
    path('api/',include(router_asociations.urls)),
    path('api/',include(router_contactCard.urls)),
    path('api/',include(router_webprofile.urls)),
    path('api/',include(router_exhibition.urls)),
    path('api/',include(router_photosexhibition.urls)),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)