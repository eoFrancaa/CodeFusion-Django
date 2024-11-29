from django.db import models


class Trimestre(models.Model):
    periodo = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.periodo}"
