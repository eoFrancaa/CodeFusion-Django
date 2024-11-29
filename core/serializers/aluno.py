from attrs import field
from cffi import model
from dill.tests.test_recursive import Model
from rest_framework.serializers import ModelSerializer

from core.models import Aluno


class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = ["id", "nome", "email"]


class AlunoInfoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        field = "__all__"
        depth = 1


class AlunoListSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        field = ["matricula", "turma"]
