from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import Turma


class TurmaSerializer(ModelSerializer):
    class Meta:
        model = Turma
        fields = "__all__"


class TurmaListSerializer(ModelSerializer):
    class Meta:
        model = Turma
        fields = ["id", "nome", "curso", "disciplina"]
