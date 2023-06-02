from django.db import models

class Post(models.Model):
    '''Данные о записи'''
    title = models.CharField('Заголовок записи', max_length=50)
    descriptions = models.TextField('Описание', max_length=1000)
    author = models.CharField('Имя автора', max_length=100)
    date = models.DateField('Дата публикации')
    image = models.ImageField('Картинка', upload_to='image/')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


