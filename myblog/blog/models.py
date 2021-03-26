from django.contrib.auth import get_user_model
from django.db import models


class Entrada(models.Model):

    titulo = models.CharField('título', max_length=140)

    texto = models.TextField('texto', max_length=1000)

    autor = models.ForeignKey(
        get_user_model(), models.CASCADE, null=True, blank=True
    )
