from django.shortcuts import render
from django.utils import timezone

from blog.models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context_data = {
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context_data)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context_data = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context_data)
