from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #link pra outro modelo
    title = models.CharField(max_length=200) #texto com tamanho 200
    text = models.TextField() #texto sem tamanho fixo
    created_date = models.DateTimeField(default=timezone.now) #data e hora
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):  #retorna uma string com o titulo do post
        return self.title

