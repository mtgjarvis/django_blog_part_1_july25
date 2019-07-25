from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def root(request):
    return HttpResponseRedirect('home')

def home_page(request):
    context = {'current_time': datetime.now()}
    response = render(request, 'index.html', context)
    return HttpResponse(response)

