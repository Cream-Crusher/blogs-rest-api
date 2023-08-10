from django.db import models
from django.utils import timezone


class Blog:
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
    uodated_at = models.DateTimeField(
        'Дата последнего обновления',
        default=timezone.now,
        db_index=True)
    authors = models.ManyToManyField(
        User,
        verbose_name='Автор(ы)',
        related_name="owners")
    owner = models.CharField(
        'ФИО владельца',
        max_length=200)


class Tag:
    tag_name = models.CharField(
        'Назвнаие тега',
        max_length=20,
        db_index=True)


class Post:
    POST_TYPES = (
        (True, 'Опубликован'),
        (False, 'не опубликован'),
    )
    author = models.ForeignKey(
        Blog,
        null=True,
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

    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    tags = models.ManyToManyField(
        Tag,
        related_name="tags",
        verbose_name='Теги',
        blank=True)


class Comment:
    authors = models.CharField(
        'Назвнаие блога',
        max_length=50,
        db_index=True)
    body = models.TextField('комментарий')
    created_at = models.DateTimeField(
        'Когда написанн комментарий',
        default=timezone.now,
        db_index=True)


class User:
    USER_TYPES = (
        (True, ' Администратор'),
        (False, 'Не админимтратор'),
    )
    user_name = models.CharField('Никнейм', max_length=200)
    is_admin = models.BooleanField(
        'Статус пользователя',
        choices=USER_TYPES,
        db_index=True,
        default='False',
        null=True)
