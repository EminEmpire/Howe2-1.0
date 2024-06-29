from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField(default=timezone.now, blank=True)
    image = models.ImageField(upload_to='blogimages/', blank=True, null=True)

    def __str__(self):
        return self.title