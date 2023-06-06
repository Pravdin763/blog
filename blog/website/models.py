from django.db import models

class Post(models.Model):
    '''Данные о записи'''
    title = models.CharField('Заголовок записи', max_length=100)
    descriptions = models.TextField('Описание', max_length=1500)
    author = models.CharField('Имя автора', max_length=100)
    date = models.DateField('Дата публикации')
    image = models.ImageField('Картинка', upload_to='image/')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Comments(models.Model):
    '''Создание комментариев'''
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comment = models.TextField('Текст комментария', max_length=200)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.email}, {self.post}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class Likes(models.Model):
    '''лайки'''
    ip = models.CharField('IP-адрес', max_length=100)
    pos = models.ForeignKey(Post, verbose_name='Публекация', on_delete=models.CASCADE)

