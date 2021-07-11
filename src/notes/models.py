from django.conf import settings
from django.db import models


class Notes(models.Model):
    name = models.CharField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    text = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.name} || {self.user}'
