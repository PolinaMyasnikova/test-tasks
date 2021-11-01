from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import *


def index(request):
    posts = Women.objects.all()
    context = {
        'title': 'MMMAAAIIINNN',
        'posts': posts,
        'vil_selected': 0,
    }
    return render(request, 'women/index.html', context=context)

def about(request):
    context = {
        'title': 'AABBOOUUTT',
    }
    return render(request, 'women/about.html', context=context)

def add_page(request):
    return HttpResponse('llllll')

def contact(request):
    return HttpResponse('llllll')

def login(request):
    return HttpResponse('llllll')

def show_cat(request, cat_slug):
    post = get_object_or_404(Women, slag=cat_slug)

    context = {
        'title': post.title,
        'post': post,
        'vil_selected': post.vil_id,
    }

    return render(request, 'women/post.html', context=context)

def pageNotFaund(request, exception):
    return HttpResponseNotFound('<h1>Страница не неадена</h1>')

def show_category(request, vil_id):
    posts = Women.objects.filter(vil_id=vil_id)

    if len(posts) == 0:
        return Http404()

    context = {
        'title': 'Отображение по рубрикам',
        'posts': posts,
        'vil_selected': vil_id,
    }
    return render(request, 'women/index.html', context=context)
