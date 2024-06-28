from django.contrib import admin
from image_cropping import ImageCroppingMixin
from .models import BlogPost, BlogImage

class BlogPostAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogImage)