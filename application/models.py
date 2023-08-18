from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count


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
        'Назвнаие тега',
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
        related_name='posts',
        verbose_name='Автор поста')
    title = models.CharField(
        'Назвнаие заголовка',
        max_length=50,
        db_index=True)
    body = models.TextField('Текст поста')
    is_published = models.BooleanField(
        'Статус публикации поста',
        choices=POST_TYPES,
        default='False',
        null=True)
    created_at = models.DateTimeField(
        'Когда создан пост',
        auto_now_add=True)

    views = models.IntegerField(default=0)

    tags = models.ManyToManyField(
        Tag,
        related_name='tags',
        verbose_name='Теги',
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
        'Назвнаие блога',
        max_length=50,
        db_index=True)
    description = models.CharField(
        'Описание блога',
        max_length=50,
        blank=True)
    created_at = models.DateTimeField(
        'Когда создан блог',
        auto_now_add=True)
    updated_at = models.DateTimeField(
        'Дата последнего обновления',
        auto_now=True)
    authors = models.ManyToManyField(
        User,
        verbose_name='Автор(ы)',
        related_name='authors')
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='owners')
    posts = models.ManyToManyField(
        Post,
        verbose_name='Посты блога',
        related_name='posts',
        blank=True)

    objects = BlogQuerySet.as_manager()

    def __str__(self):
        return self.title


class User(User):
    USER_TYPES = (
        (True, ' Администратор'),
        (False, 'Не админимтратор'),
    )
    is_admin = models.BooleanField(
        'Статус пользователя',
        choices=USER_TYPES,
        db_index=True,
        default='False',
        null=True)
    subscriptions = models.ManyToManyField(
        Blog,
        related_name='subscription_blogs',
        verbose_name='ПОдписки',
        blank=True
    )


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор Комментария')
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='пост Комментария')
    body = models.TextField('комментарий')
    created_at = models.DateTimeField(
        'Когда написанн комментарий',
        auto_now_add=True,
        db_index=True)

    def __str__(self):
        return self.authors
