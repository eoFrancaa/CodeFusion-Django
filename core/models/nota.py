from django.db import models

from .aluno import Aluno
from .disciplina import Disciplina
from .trimestre import Trimestre


class Nota(models.Model):
    trimestre = models.ForeignKey(Trimestre, on_delete=models.PROTECT)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.id} {self.valor} {self.disciplina} {self.trimestre}"
