from django.db import models

from ckeditor.fields import RichTextField


class News(models.Model):
    name = models.CharField('Заголовок', max_length=500)
    description = RichTextField('Описание')
    create_at = models.DateTimeField('Время создания', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        
    def __str__(self) -> str:
        return f'{self.name} || {self.create_at}'