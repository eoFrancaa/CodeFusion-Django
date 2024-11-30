from django.db import models

from .curso import Curso
from .disciplina import Disciplina


class Turma(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, blank=True)
    disciplina = models.ManyToManyField(Disciplina, blank=True)

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.curso.nome}"
