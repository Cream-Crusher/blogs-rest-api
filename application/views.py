from django.shortcuts import render
from application.models import Blog, Post, User
from django.contrib.auth.decorators import login_required


def serialize_blog(blog):

    return {
        'title': blog.title,
        'description': blog.description,
        'created_at': blog.created_at,
        'updated_at': blog.updated_at,
        'authors': [author.user for author in blog.author.all()],
        'owner': blog.owner
    }


def serialize_post(post):

    return {
        'author': post.author,
        'title': post.title,
        'body': post.body,
        'is_published': post.is_published,
        'created_at': post.created_at,
        'likes': post.likes,
        'views': post.views,
        'tags': [serialize_tag(tag) for tag in post.tags.all()],
    }


def serialize_tag(tag):

    return {
        'title': tag.tag_name,
    }


def show_home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': [serialize_blog(blog) for blog in blogs]
    }

    return render(request, 'home.html', context)


def show_blog(request):
    blogs = Blog.objects.all().order_by('updated_at')
    context = {
        'blogs': [serialize_blog(blog) for blog in blogs]
    }

    return render(request, 'blog.html', context)


def show_post(request):
    posts = Post.objects.all().filter(is_published=True).order_by('created_at')
    context = {
        'posts': [serialize_post(post) for post in posts]
    }

    return render(request, 'post.html', context)


@login_required(login_url='/accounts/login/')
def show_user_post(request):
    posts = Post.objects.filter(author=request.user)
    context = {
        'posts': [serialize_post(post) for post in posts]
    }

    return render(request, 'user_post.html', context)


@login_required(login_url='/accounts/login/')
def show_user_blog(request):
    user = User.objects.get(username=request.user)
    blogs = user.authors.all()

    context = {
        'blogs': [serialize_blog(blog) for blog in blogs]
    }

    return render(request, 'blog.html', context)
