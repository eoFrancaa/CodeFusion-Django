from attrs import field
from cffi import model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import Turma


class TurmaSerializer(ModelSerializer):
    class Meta:
        model = Turma
        fields = "__all__"


class TurmaListSerializer(ModelSerializer):
    ano = serializers.IntegerField(source="ano.data")

    class Meta:
        model = Turma
        fields = ["id", "nome", "curso", "ano"]
