from django.shortcuts import render
from .models import Comment, Article, Person

def lastFiveComment(request):
    lastCommentid = Comment.objects.last().id
    b = Comment.objects.filter(id__lte=lastCommentid).order_by('-id')[:5]
    return render(request, 'main_blog.html', {'a': b})

def first_2_comments_by_last_author(request):
    author = Person.objects.all().order_by('-name')[0]
    article = Article.objects.filter(author=author)[0]
    comments = Comment.objects.filter(article=article).order_by('created_at')[:2]
    return render(request, 'first_2_comments_by_last_author.html', {'comments':comments})