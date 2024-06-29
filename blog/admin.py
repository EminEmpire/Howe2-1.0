from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    fields = ('title', 'content', 'published_date', 'image')
    ordering = ('-published_date',)