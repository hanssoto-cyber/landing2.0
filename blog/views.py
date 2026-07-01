from django.shortcuts import render, get_object_or_404
from .models import Post


def lista_posts(request):
    posts = Post.objects.filter(publicado=True)
    return render(request, 'blog/lista.html', {'posts': posts})


def detalle_post(request, slug):
    post = get_object_or_404(Post, slug=slug, publicado=True)
    return render(request, 'blog/detalle.html', {'post': post})