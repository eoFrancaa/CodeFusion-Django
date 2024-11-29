from attrs import field
from cffi import model
from rest_framework.serializers import ModelSerializer

from core.models import Turma


class TurmaSerializer(ModelSerializer):
    class Meta:
        model = Turma
        fields = ["nome", "curso", "ano"]


class TurmaListSerializer(ModelSerializer):
    class Meta:
        model = Turma
        field = ["nome", "curso", "ano"]
