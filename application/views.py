from django.shortcuts import render
from application.models import Blog, Post, User
from django.contrib.auth.decorators import login_required
from django.core import serializers


def get_count_like(post):
    return post.posts_count


def show_home(request):
    blogs = Blog.objects.order_by('updated_at').loading_db_queries()
    context = {
        'blogs': serializers.serialize('json', list(blogs))
    }

    return render(request, 'home.html', context)


def show_blog(request):
    blogs = Blog.objects.order_by('created_at').loading_db_queries()
    context = {
        'blogs': serializers.serialize('json', list(blogs))
    }

    return render(request, 'blog.html', context)


def show_post(request):
    posts = Post.objects.filter(is_published=True).count_like().loading_db_queries()
    context = {
        'posts': serializers.serialize('json', list(posts)),
        'likes': [get_count_like(post) for post in posts],
    }

    return render(request, 'post.html', context)


@login_required(login_url='/accounts/login/')
def show_user_post(request):
    posts = Post.objects.filter(author=request.user).count_like().loading_db_queries()
    context = {
        'posts': serializers.serialize('json', list(posts)),
        'likes': [get_count_like(post) for post in posts],
    }

    return render(request, 'user_post.html', context)


@login_required(login_url='/accounts/login/')
def show_user_blog(request):
    blogs = Blog.objects.filter(authors=request.user).order_by('created_at').loading_db_queries()
    context = {
        'blogs': serializers.serialize('json', list(blogs))
    }

    return render(request, 'blog.html', context)
