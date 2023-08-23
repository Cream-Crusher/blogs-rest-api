from django.contrib.auth.models import User
from django.db.models import Count
from django.db import models


class PostQuerySet(models.QuerySet):

    def loading_db_queries(self):  # Оптимизация запросов к DB

        return self.prefetch_related('author', 'tags')

    def count_like(self):

        return self.annotate(like_count=Count('likes'))


class BlogQuerySet(models.QuerySet):

    def loading_db_queries(self):  # Оптимизация запросов к DB

        return self.prefetch_related('authors', 'owner', 'posts')


class Tag(models.Model):
    tag_name = models.CharField(
        max_length=20,
        unique=True)

    def __str__(self):
        return self.tag_name


class Post(models.Model):
    POST_TYPES = (
        (True, 'Опубликован'),
        (False, 'не опубликован'),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts')
    title = models.CharField(
        max_length=50,
        db_index=True)
    body = models.TextField()
    is_published = models.BooleanField(
        choices=POST_TYPES,
        default='False',
        null=True)
    created_at = models.DateTimeField(
        auto_now_add=True)
    views = models.IntegerField(default=0)
    tags = models.ManyToManyField(
        Tag,
        related_name='tags',
        blank=True)
    likes = models.ManyToManyField(
        User,
        blank=True,
        related_name='post_like'
        )

    objects = PostQuerySet.as_manager()

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(
        max_length=50,
        db_index=True)
    description = models.CharField(
        max_length=50,
        blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True)
    authors = models.ManyToManyField(
        User,
        related_name='authors')
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owners')
    posts = models.ManyToManyField(
        Post,
        related_name='posts',
        blank=True)

    objects = BlogQuerySet.as_manager()

    def __str__(self):
        return self.title


class User(User):
    subscriptions = models.ManyToManyField(
        Blog,
        related_name='subscription_blogs',
        blank=True
    )


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments')
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True)

    def __str__(self):
        return self.authors
