from django.db import models

from .disciplina import Disciplina


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    disciplina = models.ManyToManyField(Disciplina, blank=True)

    def __str__(self):
        return f"{self.id} - {self.nome}"
