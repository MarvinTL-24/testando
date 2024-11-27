from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils import timezone


    # Create your models here.
class Question(models.Model):
    perguntas = models.CharField(max_length=200)
    publicar = models.DateTimeField('Dia de publicar')
    def __str__(self):
        return self.perguntas
    def was_published_recently(self):
        return self.publicar >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    respostas = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    def __str__(self):
        return self.respostas
