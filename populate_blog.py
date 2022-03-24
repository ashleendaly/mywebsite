import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'mywebsite.settings')

import django
django.setup()
from blog.models import Category, Post


def populate():

    django_posts = [
        {'title': 'How I Build A Blog From Scratch For Free Using Django',
         'text': 'It was easy!'}
    ]

    crypto_pages = [
        {'title': 'Understanding Smart Contracts',
         'text': '1 + 1 = 2'}
    ]

    cats = {'Django Builds': {'posts': django_posts},
            'Cryptocurrency': {'posts': crypto_pages}
            }

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['posts']:
            add_post(c, p['title'], p['text'])

    for c in Category.objects.all():
        for p in Post.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_post(cat, title, text, views=0, likes=0):
    p = Post.objects.get_or_create(category=cat, title=title, text=text, likes=likes)[0]
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


if __name__ == '__main__':
    print('Starting Blog population script...')
    populate()
