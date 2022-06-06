from django.urls import path
from .views import main_article, some_articles_archive, some_article_number_slug

urlpatterns = [
    path('', main_article, name='article'),
    path('archive/', some_articles_archive),
    path('<int:article_number>', some_article_number_slug),
    path('<int:article_number>/<slug:slug_text>', some_article_number_slug)
]