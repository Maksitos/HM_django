from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=80)


class Catalog(models.Model):
    title = models.CharField(max_length=80)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Authorinlib(models.Model):
    name = models.CharField(max_length=80)

class Booksinlib(models.Model):
    title = models.CharField(max_length=80)
    authors = models.ManyToManyField(Authorinlib)
    available = models.BooleanField()