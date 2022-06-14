from django.urls import path
from .views import lastFiveComment, first_2_comments_by_last_author
urlpatterns = [
    path('last-five-comments', lastFiveComment),
    path('first-2-comments-by-last-author', first_2_comments_by_last_author)
]