from django.db import models


class Ano(models.Model):
    data = models.CharField(max_length=4)

    def __str__(self):
        return f"({self.data})"
