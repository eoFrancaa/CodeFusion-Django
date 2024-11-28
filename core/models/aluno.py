from django.db import models

from .turma import Turma


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=False, null=True)
    turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
      return f"{self.id} - {self.nome} - {self.turma.nome} - {self.email}"
    
