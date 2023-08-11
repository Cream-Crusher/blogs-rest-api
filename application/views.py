from django.shortcuts import render
from application.models import Blog, Post


def show_home(request):
    blogs = Blog.objects.all()
    processed_blogs = []

    for blog in blogs:  # TODO Вынести в функцию
        processed_blogs.append({
            'title': blog.title,
            'description': blog.description,
            'created_at': blog.created_at,
            'updated_at': blog.updated_at,
            'authors': blog.authors,
            'owner': blog.owner,
            'detailsUrl': None  # TODO  Реализовать

        })

    return render(request, 'home.html', context={'blogs': processed_blogs})


def show_blog(request):
    blogs = Blog.objects.all().order_by('updated_at')
    processed_blogs = []

    for blog in blogs:  # TODO Вынести в функцию
        processed_blogs.append({
            'title': blog.title,
            'description': blog.description,
            'created_at': blog.created_at,
            'updated_at': blog.updated_at,
            'authors': blog.authors,
            'owner': blog.owner,
            'detailsUrl': None  # TODO  Реализовать

        })

    return render(request, 'home.html', context={'blogs': processed_blogs})


def show_posts(request):
    posts = Post.objects.all().filter(is_published=True).order_by('created_at')
    processed_posts = []

    for post in posts:  # TODO Вынести в функцию
        processed_posts.append({
            'author': post.author,
            'title': post.title,
            'body': post.body,
            'is_published': post.is_published,
            'created_at': post.created_at,
            'likes': post.likes,
            'views': post.views,
            'tags': post.tags,
            'detailsUrl': None  # TODO  Реализовать
        })

    return render(request, 'post.html', context={'posts': processed_posts})


def user_posts(request):
    posts = Post.objects.all().filter(author='#')
    processed_posts = []

    for post in posts:  # TODO Вынести в функцию
        processed_posts.append({
            'author': post.author,
            'title': post.title,
            'body': post.body,
            'is_published': post.is_published,
            'created_at': post.created_at,
            'likes': post.likes,
            'views': post.views,
            'tags': post.tags,
            'detailsUrl': None  # TODO  Реализовать
        })

    return render(request, 'user_home.html', context={'posts': processed_posts})
