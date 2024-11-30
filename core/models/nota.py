from django.db import models

from .aluno import Aluno
from .disciplina import Disciplina
from .turma import Turma


class Nota(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.id} {self.valor} {self.disciplina}"
