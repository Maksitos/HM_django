from django.urls import path
from .views import main_article, some_articles_archive, some_article_number_slug, some_article_number_archive

urlpatterns = [
    path('', main_article, name='main_articles'),
    path('archive/', some_articles_archive),
    path('<int:article_number>', some_article_number_slug, name='article'),
    path('<int:article_number>/archive', some_article_number_archive),
    path('<int:article_number>/<slug:slug_text>', some_article_number_slug, name='article_slug')
]