from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': ' How I Made A Blog For Free Using Django'}
    return render(request, 'blog/index.html', context=context_dict)


def about(request):
    return render(request, 'about.html')

