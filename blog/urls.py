from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:category_name_slug>/',
         views.show_category, name="show_category"),
    path('<slug:category_name_slug>/<slug:post_title_slug>/',
         views.show_post, name="show_post")
]