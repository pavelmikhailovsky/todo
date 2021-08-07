from django.conf import settings
from django.db import models


class Notes(models.Model):
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    # update_at = models.CharField(default='Ещё не редактировался')
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.create_at} || {self.user}'
    
    class Meta:
        verbose_name = 'заметку'
        verbose_name_plural = 'Заметки'
