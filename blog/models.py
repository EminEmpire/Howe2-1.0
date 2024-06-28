from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from image_cropping import ImageCropField, ImageRatioField

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateField(null=True, blank=True)  # Changed to DateField
    thumbnail = ImageCropField(upload_to='thumbnails/')
    cropping = ImageRatioField('thumbnail', '300x300')
    thumbnail_square = ImageSpecField(source='thumbnail',
                                      processors=[ResizeToFill(300, 300)],
                                      format='JPEG',
                                      options={'quality': 90})

    def __str__(self):
        return self.title
    
class BlogImage(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption