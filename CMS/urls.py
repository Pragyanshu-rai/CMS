"""CMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from cms import views as cms_views
from django.contrib import admin

from django.urls import path, include

from django.conf import settings

from django.conf.urls.static import static
from django.urls.conf import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cms/', include('cms.urls')),
    path('cms-api/', include('cms_api.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# must change the view which must be called
urlpatterns += [
    re_path(r'(?P<path>.*)', cms_views.error)
]
