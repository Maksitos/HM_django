from django.urls import path
from .views import main_article, some_articles_archive, some_article_number, some_article_number_archive

urlpatterns = [
    path('', main_article),
    path('archive/', some_articles_archive),
    path('<int:article_number>', some_article_number),
    path('<int:article_number>/archive', some_article_number_archive)
]