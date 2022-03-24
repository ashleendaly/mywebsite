from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Featured Categories'
    context_dict['categories'] = category_list

    return render(request, 'blog/index.html', context=context_dict)


def about(request):
    return render(request, 'about.html')


def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        posts = Post.objects.filter(category=category)

        context_dict['posts'] = posts
        context_dict['category'] = category
    except:
        context_dict['posts'] = None
        context_dict['category'] = None

    return render(request, 'blog/category.html', context=context_dict)


def show_post(request, category_name_slug, post_title_slug):
    context_dict = {}

    try:
        post = Post.objects.filter(slug=post_title_slug)
        context_dict['post'] = post

    except:
        context_dict['post'] = None

    return render(request, 'blog/post.html', context=context_dict)
