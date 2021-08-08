from datetime import datetime

from django.conf import settings
from django.db import models


# TODO change create_at and update_at -> DD:MM:YYYY HH:MM:SS
class Notes(models.Model):
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.CharField(default='Не редактирован', max_length=300)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__text = self.text

    def __str__(self) -> str:
        return f'{self.create_at} || {self.user}'

    def save(self, *args, **kwargs):
        if self.__text != self.text:
            self.update_at = f'{datetime.now()}'
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'заметку'
        verbose_name_plural = 'Заметки'
        db_table = 'notes'
