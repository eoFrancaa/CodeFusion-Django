from django.db import models

from black import mode

from .ano import Ano
from .curso import Curso


class Turma(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, blank=True)
    ano = models.ForeignKey(Ano, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.curso.nome} {self.ano_data}"
