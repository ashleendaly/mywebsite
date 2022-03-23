from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Ash On The Internet")

# Create your views here.
