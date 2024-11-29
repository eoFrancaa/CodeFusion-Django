from attrs import field
from cffi import model
from dill.tests.test_recursive import Model
from jsonschema._keywords import required
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import Professor
from uploader.models import Image
from uploader.serializers import ImageSerializer


class ProfessorSerializer(ModelSerializer):
    class Meta:
        model = Professor
        fields = ["id", "nome", "email"]
        capa_attachment_key = SlugRelatedField(
            source="capa",
            queryset=Image.objects.all(),
            slug_field="attachment_key",
            required=False,
            write_only=True,
        )

    capa = ImageSerializer(required=False, read_only=True)


class ProfessorInfoSerializer(ModelSerializer):
    class Meta:
        model = Professor
        fields = "__all__"


class ProfessorListSerializer(ModelSerializer):
    class Meta:
        model = Professor
        fields = "__all__"
        capa = ImageSerializer(required=False)
