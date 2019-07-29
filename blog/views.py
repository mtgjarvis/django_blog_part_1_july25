from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import Article


def root(request):
    return HttpResponseRedirect('home')


def home_page(request):
    date = datetime.now().date()
    all_articles = Article.objects.order_by("-published_date")
    context = {'articles': all_articles, 'date': date}
    response = render(request, 'index.html', context)
    return HttpResponse(response)
