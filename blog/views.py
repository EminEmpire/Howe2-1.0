from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.
def blog_list(request):
    posts = BlogPost.objects.order_by('-published_date')
    return render(request, 'blog_list.html', {'posts': posts})

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    next_post = BlogPost.objects.filter(published_date__gt=post.published_date).order_by('published_date').first()
    previous_post = BlogPost.objects.filter(published_date__lt=post.published_date).order_by('-published_date').first()
    return render(request, 'blog_detail.html', {'post': post, 'next_post': next_post, 'previous_post': previous_post})