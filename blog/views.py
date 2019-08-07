from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import Article, ArticleForm, Comment, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from blog.forms import LoginForm, Form
from django.contrib.auth.decorators import login_required


def root(request):
    return HttpResponseRedirect('/home')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/home')
    else:
        form = UserCreationForm()
    html_response = render(request, 'signup.html', {'form': form})
    return HttpResponse(html_response)


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=username, password=pw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home')
            else:
                form.add_error('username', 'Login Failed')
    else:
        form = LoginForm()

    context = {'form': form}
    http_response = render(request, 'login.html', context)
    return HttpResponse(http_response)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')


# def create(request):
#     form = ArticleForm()
#     form.save()
#     return HttpResponseRedirect("/home")


def home_page(request):
    date = datetime.now().date()
    blogs = Article.objects.all()
    context = {'blogs': blogs, 'date': date}
    return render(request, 'index.html', context)


def show(request, id):
    article = Article.objects.get(pk=id)
    context = {"article": article}
    return render(request, "show.html", context)

@login_required
def create_comment(request):
    article_id = request.POST['article']
    article = Article.objects.filter(id=article_id).first()
    # name = request.POST['name']
    # message = request.POST['message']
    # new_comment = Comment(article=article, name=name, message=message)
    # new_comment.save()
    form = CommentForm(request.POST)
    context = {'article': article, 'form': form}
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.article = article
        form.save()
        return HttpResponseRedirect(f'/home/{article_id}')
    else:
        return render(request, 'show.html', context)

@login_required
def new_article(request):
    form = ArticleForm(request.POST)
    context = {"form": form, "message": "Create New Article", "action": "create_article"}
    if request.method == "POST":
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return HttpResponseRedirect("/home")
    # return render(request, 'show.html', context)
    
    return render(request, "form.html", context)

@login_required
def create_article(request):
    form = ArticleForm(request.POST)
    form.save()
    return HttpResponseRedirect("/home")

# def post_show(request):
#     article = Article.objects.get(pk=id)
#     context = {'article': article}
#     return render(request, '')