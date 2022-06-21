from django.shortcuts import render
from .models import Comment, Article, Person
from .forms import GetComments, Form, AuthenticationForm, RegistrationForm, PassChangeForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def lastFiveComment(request):
    lastCommentid = Comment.objects.last().id
    b = Comment.objects.filter(id__lte=lastCommentid).order_by('-id')[:5]
    return render(request, 'main_blog.html', {'a': b})

def first_2_comments_by_last_author(request):
    author = Person.objects.all().order_by('-name')[0]
    article = Article.objects.filter(author=author)[0]
    comments = Comment.objects.filter(article=article).order_by('created_at')[:2]
    return render(request, 'first_2_comments_by_last_author.html', {'comments':comments})

@login_required(login_url='/blog/login')
def form(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            text = 'You meet our requirements.'
        else:
            text = 'You do not meet our requirements.'
        return render(request, 'after_form.html', {'text': text})
    else:
        form = Form()
        return render(request, 'form.html', {'form': form, 'user': request.user})


def my_login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AuthenticationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # some actions
            login(request, form.user)
            return HttpResponseRedirect('/blog/form')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def my_logout(request):
    logout(request)
    return HttpResponseRedirect('/blog/login')


def my_register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            new_user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, new_user)
            return HttpResponseRedirect('/blog/form')
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})

@login_required(login_url='/blog/login')
def pass_change(request):

    if request.method == 'POST':
        form = PassChangeForm(request.POST)

        if form.is_valid():
            u = request.user
            if u.check_password(raw_password=form.cleaned_data['password']) and u.check_password(raw_password=form.cleaned_data['rep_password']):
                new_pass = form.cleaned_data['new_password']
                u.set_password(raw_password=new_pass)
                u.save()
                return HttpResponseRedirect('/blog/form')
    else:
        form = PassChangeForm()
    return render(request, 'pass_change.html', {'form': form})


def get_comment(request):
    form = GetComments()
    return render(request, 'get_comment_form.html', {'form': form})


def comments(request):
    some_word = request.GET['some_words']
    user = request.user
    if 'only_user_com' in request.GET:
        comments = Comment.objects.filter(text__contains=some_word, user=user)
    else:
        comments = Comment.objects.filter(text__contains=some_word)
    return render(request, 'comments.html', {'comments':comments})
