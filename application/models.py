from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Count  # , Prefetch


class PostQuerySet(models.QuerySet):

    def count_likes(self):

        return self.annotate(posts_count=Count('liked_posts'))


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
        default=timezone.now,
        db_index=True)
    updated_at = models.DateTimeField(
        'Дата последнего обновления',
        default=timezone.now,
        db_index=True)
    authors = models.ManyToManyField(
        User,
        verbose_name='Автор(ы)',
        related_name='authors')
    owner = models.CharField(
        'ФИО владельца',
        max_length=200)

    def __str__(self):
        return self.title


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
        db_index=True,
        default='False',
        null=True)
    created_at = models.DateTimeField(
        'Когда создан пост',
        db_index=True)

    views = models.IntegerField(default=0)
    tags = models.ManyToManyField(
        Tag,
        related_name='tags',
        verbose_name='Теги',
        blank=True)

    objects = PostQuerySet.as_manager()

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
    liked_post = models.ManyToManyField(
        Post,
        related_name='liked_posts',
        verbose_name='Лайкнутые посты',
        blank=True
    )
    subscriptions = models.ManyToManyField(
        Blog,
        related_name='subscription_blogs',
        verbose_name='ПОдписки',
        blank=True
    )


class Comment(models.Model):
    authors = models.CharField(
        'Автор',
        max_length=50,
        db_index=True)
    body = models.TextField('комментарий')
    created_at = models.DateTimeField(
        'Когда написанн комментарий',
        default=timezone.now,
        db_index=True)

    def __str__(self):
        return self.authors
