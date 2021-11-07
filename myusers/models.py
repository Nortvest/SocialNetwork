from django.db import models
from django.contrib.auth.models import AbstractUser


class UsersModel(AbstractUser):
    """Главная модель пользователей на основе AbstractUser"""
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, max_length=1024, verbose_name='Фото')
    slug = models.SlugField(max_length=64, unique=True, db_index=True, verbose_name='URL', blank=True, null=True)
    about = models.TextField(null=True, verbose_name='Обо мне')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'Users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
