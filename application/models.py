from django.db import models
from django.utils import timezone


class User(models.Model):
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

    def str(self):
        return self.user_name


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
        related_name="owners")
    owner = models.CharField(
        'ФИО владельца',
        max_length=200)

    def str(self):
        return self.title


class Tag(models.Model):
    tag_name = models.CharField(
        'Назвнаие тега',
        max_length=20,
        unique=True)

    def str(self):
        return self.tag_name


class Post(models.Model):
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
        related_name='tags',
        verbose_name='Теги',
        blank=True)

    def str(self):
        return self.author


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

    def str(self):
        return self.authors
