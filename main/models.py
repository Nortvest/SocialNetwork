from django.db import models


class TypeMediaModel(models.Model):
    type_media = models.CharField(max_length=128, unique=True, verbose_name='Тип медиа')

    def __str__(self):
        return self.type_media

    class Meta:
        db_table = 'TypeMedia'
        verbose_name = 'Тип медиа файла'
        verbose_name_plural = 'Типы медиа файлов'


class PostsModel(models.Model):
    """Модель постов"""
    text = models.TextField(blank=True, verbose_name='Текст поста')
    media = models.FileField(upload_to='media_post', blank=True, verbose_name='Медиа файл')
    type_media = models.ForeignKey(to=TypeMediaModel, on_delete=models.PROTECT, verbose_name='Тип медиа файла',
                                   null=True, blank=True)
    own = models.ForeignKey(to='myusers.UsersModel', on_delete=models.PROTECT, verbose_name='Хозяин поста')

    def __str__(self):
        return self.own.username

    class Meta:
        db_table = 'Posts'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class LikesModel(models.Model):
    """Модель лайков на постах"""
    user = models.ForeignKey(to='myusers.UsersModel', on_delete=models.PROTECT, verbose_name='Пользователя')
    post = models.ForeignKey(to=PostsModel, on_delete=models.PROTECT, verbose_name='Пост')

    class Meta:
        db_table = 'Likes'
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'


class CommentsModel(models.Model):
    """Модель коментариев на остах"""
    text = models.TextField()
    user = models.ForeignKey(to='myusers.UsersModel', on_delete=models.PROTECT, verbose_name='Пользователь')
    post = models.ForeignKey(to=PostsModel, on_delete=models.PROTECT, verbose_name='Пост')

    class Meta:
        db_table = 'Comments'
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'


class FollowersModel(models.Model):
    """Модель подписчиков"""
    user = models.ForeignKey(to='myusers.UsersModel', related_name='+', on_delete=models.PROTECT,
                             verbose_name='Пользователь')
    user2 = models.ForeignKey(to='myusers.UsersModel', on_delete=models.PROTECT, verbose_name='Подписчик')

    class Meta:
        db_table = 'Followers'
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
