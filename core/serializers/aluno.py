from attrs import field
from cffi import model
from dill.tests.test_recursive import Model
from jsonschema._keywords import required
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import Aluno
from uploader.models import Image
from uploader.serializers import ImageSerializer


class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = ["id", "nome", "email"]
        capa_attachment_key = SlugRelatedField(
            source="capa",
            queryset=Image.objects.all(),
            slug_field="attachment_key",
            required=False,
            write_only=True,
        )

    capa = ImageSerializer(required=False, read_only=True)


class AlunoInfoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = "__all__"
        depth = 1


class AlunoListSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = ["nome", "matricula", "turma"]
        capa = ImageSerializer(required=False)
