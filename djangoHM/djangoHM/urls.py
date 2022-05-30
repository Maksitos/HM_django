"""djangoHM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
from myapp.views import main, users, some_user_number, regular, phone

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('users/', users),
    path('articles/', include('myapp.urls')),
    path('users/<int:user_number>', some_user_number),
    re_path(r'^(?P<text>[1-9a-f]{4}-[a-zA-Z0-9]{6}$)',regular),
    re_path(r'^(?P<number>0(63|50|93|66)\d{7}$)', phone)
]
