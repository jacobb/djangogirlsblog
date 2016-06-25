from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from blog.forms import PostForm
from blog.models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context_data = {
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context_data)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context_data = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context_data)


def post_new(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        return redirect('post_detail', pk=post.pk)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
