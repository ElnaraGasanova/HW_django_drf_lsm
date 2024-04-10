from django.db import models
from users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование', help_text='Укажите наименование курса')
    image = models.ImageField(upload_to='courses_image', verbose_name='Превью', help_text='Загрузите превью курса',
                              **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        '''Добавляем строковое отображение это будет выводиться на сайте в карточке!'''
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
