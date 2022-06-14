from django.urls import path
from .views import main_blog
urlpatterns = [
    path('', main_blog, name='main_blog'),
]