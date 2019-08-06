from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import Article, ArticleForm, Comment, CommentForm


def root(request):
    return HttpResponseRedirect('/home')


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


def create_comment(request):
    article_id = request.POST['article']
    article = Article.objects.filter(id=article_id).first()
    name = request.POST['name']
    message = request.POST['message']
    new_comment = Comment(article=article, name=name, message=message)
    new_comment.save()
    # form = CommentForm(request.POST)
    # context = []
    return HttpResponseRedirect(f'/home/{article_id}')


def new_article(request):
    form = ArticleForm()
    context = {"form": form, "message": "Create New Article", "action": "create_article"}
    return render(request, "form.html", context)


def create_article(request):
    form = ArticleForm(request.POST)
    form.save()
    return HttpResponseRedirect("/home")

# def post_show(request):
#     article = Article.objects.get(pk=id)
#     context = {'article': article}
#     return render(request, '')