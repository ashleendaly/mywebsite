from django.contrib import admin
from blog.models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)


