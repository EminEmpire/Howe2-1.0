from django.contrib import admin
from image_cropping import ImageCroppingMixin
from .models import BlogPost, BlogImage

class BlogPostAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('title', 'published_date', 'created_at', 'updated_at')
    list_editable = ('published_date',)

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogImage)