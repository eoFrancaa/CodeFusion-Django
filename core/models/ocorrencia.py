from django.db import models

from .aluno import Aluno
from datetime import date


class Ocorrencia(models.Model):
    class Trimestre(models.IntegerChoices):
        PRIMEIRO = 1, "1º Trimestre"
        SEGUNDO = 2, "2º Trimestre"
        TERCEIRO = 3, "3º Trimestre"
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    assunto = models.CharField(max_length=300, null=True, blank=True)

    class papeis(models.IntegerChoices):
        ATRASO = 1, "Registrar Atraso"
        UNIFORME = 2, "Sem Uniforme"
        NUPE = 3, "Reunião NUPE"

    papel_ocorrencia = models.IntegerField(choices=papeis.choices, default=papeis.ATRASO, null=True, blank=True)
    trimestre = models.IntegerField(choices=Trimestre.choices, default=Trimestre.PRIMEIRO, null=True, blank=True)
    data_ocorrencia = models.IntegerField(default=date.today().year)

    def __str__(self):
        return f"({self.id}) {self.aluno.nome} ({self.papel_ocorrencia}) {self.assunto}"
