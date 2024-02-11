"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    
    # Applications
    path('', include('web.urls')),
    path('', include('accounts.urls')),
    path('', include('dashboard.urls')),
    path('panel/', include('panel.urls')),
    path('panel/social_media/', include('social_media.urls')),
    path('blog/', include('blog.urls')),
    
    
    # Swagger and Redoc
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger_ui"),
    path("swagger-json/", SpectacularAPIView.as_view(), name="schema"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

    # Captcha
    path('captcha/', include('captcha.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)