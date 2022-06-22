from django.urls import path
from .views import get_comment, comments, lastFiveComment, first_2_comments_by_last_author, form, my_login, my_logout, my_register, pass_change
urlpatterns = [
    path('last-five-comments', lastFiveComment),
    path('first-2-comments-by-last-author', first_2_comments_by_last_author),
    path('form', form, name='SomeForm'),
    path('login', my_login, name='LoginForm'),
    path('logout', my_logout, name='logout'),
    path('registration', my_register, name='registrationForm'),
    path('pass_change', pass_change, name='pass_change'),
    path('comments', comments, name='comments'),
    path('get_comment', get_comment, name='get_comment')
]