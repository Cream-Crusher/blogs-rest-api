from django.shortcuts import render
from application.models import Blog


def show_page(request):
    blogs = Blog.objects.all()
    processed_blogs = []

    for blog in blogs:
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
