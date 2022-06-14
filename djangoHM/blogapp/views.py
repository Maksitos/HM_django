from django.shortcuts import render
from django.http import HttpResponse

def main_blog(request):
    return HttpResponse('Main blog is here')