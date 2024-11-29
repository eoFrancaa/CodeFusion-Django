from django.db import models

from .ano import Ano


class Trimestre(models.Model):
    periodo = models.CharField(max_length=20)
    ano = models.ForeignKey(Ano, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.periodo} {self.ano}"
