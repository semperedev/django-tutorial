from django.db import models


class Entrada(models.Model):

    titulo = models.CharField('título', max_length=140)

    texto = models.TextField('texto', max_length=1000)
