from django.conf import settings
from django.db import models

from .utils import datetime_now


class Notes(models.Model):
    text = models.TextField()
    create_at = models.CharField(default=f'{datetime_now()}', max_length=50)
    update_at = models.CharField(default='Не редактирован', max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__text = self.text

    def __str__(self) -> str:
        return f'{self.create_at} || {self.user}'

    def save(self, *args, **kwargs):
        if self.__text != self.text:
            self.update_at = f'{datetime_now()}'
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'заметку'
        verbose_name_plural = 'Заметки'
        db_table = 'notes'
