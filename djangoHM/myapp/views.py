from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    return HttpResponse('Main page is here')


def main_article(request):
    return HttpResponse('Main articles page is here')


def some_articles_archive(request):
    return HttpResponse('Some Archive is here')


def users(request):
    return HttpResponse('Users page is here')


def some_user_number(request, user_number):
    return HttpResponse(f'User {user_number} page is here')


def some_article_number(request, article_number):
    return HttpResponse(f'Article {article_number} page is here')


def some_article_number_archive(request, article_number):
    return HttpResponse(f'{article_number} archive is here')


def regular(request, text):
    return HttpResponse(f'{text} - is the right regular')


def phone(request, number):
    return HttpResponse(f'{number} - is the right phone number')


