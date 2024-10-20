"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to view. For more information please see:
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
from django.contrib import admin
from django.urls import path

from djangoProject.views.stream_views import stream_music
from djangoProject.views.views import list_musics

urlpatterns = [
    path('admin/', admin.site.urls),
    path('play/', stream_music),
    path('musics/', list_musics),
]
