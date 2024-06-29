from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-published_date')
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    previous_post = BlogPost.objects.filter(published_date__lt=post.published_date).order_by('-published_date').first()
    next_post = BlogPost.objects.filter(published_date__gt=post.published_date).order_by('published_date').first()
    return render(request, 'blog/blog_detail.html', {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post
    })