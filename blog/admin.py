from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.utils import timezone
from .models import Category, Tag, Post

class PostAdmin(admin.ModelAdmin):
    list_display :list = ['title', 'created_time', 'modified_time', 'category', 'author']
    fields : list = ['title', 'body', 'excerpt', 'category', 'tags']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.modified_time = timezone.now()
        super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
