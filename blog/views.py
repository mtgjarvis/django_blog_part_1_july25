from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import Article, ArticleForm


def root(request):
    return HttpResponseRedirect('/home')


# def create(request):
#     form = Article.objects.get(pk=id)
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


# def post_show(request):
#     article = Article.objects.get(pk=id)
#     context = {'article': article}
#     return render(request, '')