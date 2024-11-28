from attrs import field
from dill.tests.test_recursive import Model
from pyexpat import model
from rest_framework.serializers import ModelSerializer

from core.models import Curso
from core.models.disciplina import Disciplina


class CursoSerializer(ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"


class DisciplinaCurso(ModelSerializer):
    class Meta:
        model = Disciplina
        fields = "nome"
