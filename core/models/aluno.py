from email.mime import image

from django.db import models

from uploader.models import Image

from .turma import Turma


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=False, null=True)
    matricula = models.CharField(max_length=10, null=True)
    turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True, blank=True)
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.turma.nome} - {self.email}"
