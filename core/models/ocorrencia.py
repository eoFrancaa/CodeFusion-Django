from django.db import models

from .aluno import Aluno


class Ocorrencia(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    assunto = models.CharField(max_length=300, null=True, blank=True)

    class papeis(models.IntegerChoices):
        ATRASO = 1, "Registrar Atraso"
        UNIFORME = 2, "Sem Uniforme"
        NUPE = 3, "Reunião NUPE"

    papel_ocorrencia = models.IntegerField(choices=papeis.choices, default=papeis.ATRASO, null=True, blank=True)

    def __str__(self):
        return f"({self.id}) {self.aluno.nome} ({self.papel_ocorrencia}) {self.assunto}"
