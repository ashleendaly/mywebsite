from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['boldmessage'] = ' How I Made A Blog For Free Using Django'
    context_dict['categories'] = category_list

    return render(request, 'blog/index.html', context=context_dict)


def about(request):
    return render(request, 'about.html')

