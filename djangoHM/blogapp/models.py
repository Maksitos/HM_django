from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Person(models.Model):
    name = models.CharField(max_length=100)

class Article(models.Model):
    author = models.ForeignKey(Person, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True)
    text = models.TextField(max_length=10000, null=True, blank=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField(max_length=10000, null=True)
    subcomment = models.ForeignKey('blogapp.Comment', on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    created_at = models.DateField()

    def save(self, **kwargs):
        if not self.id:
            if timezone.now().year % 4 == 0:
                self.created_at = timezone.now() - timezone.timedelta(days=366)
            else:
                self.created_at = timezone.now() - timezone.timedelta(days=365)
        super().save(**kwargs)

class Rating(models.Model):

    class Choice(models.IntegerChoices):
        LIKE = 1
        DISLIKE = 2

    choice = models.IntegerField(choices=Choice.choices)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(Person, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True)