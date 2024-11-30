from attrs import field
from cffi import model
from dill import source
from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import Aluno
from uploader.models import Image
from uploader.serializers import ImageSerializer


class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = [
            "id",
            "nome",
            "email",
        ]
        capa_attachment_key = SlugRelatedField(
            source="capa",
            queryset=Image.objects.all(),
            slug_field="attachment_key",
            required=False,
            write_only=True,
        )

    capa = ImageSerializer(required=False, read_only=True)


class AlunoInfoSerializer(ModelSerializer):
    nome = serializers.CharField()
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa_url = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="url",
    )

    class Meta:
        model = Aluno
        fields = ["nome", "email", "id", "turma", "capa_url", "capa_attachment_key"]


class AlunoImageSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa_url = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="url",
    )

    url = StringRelatedField()

    class Meta:
        model = Image
        fields = ["url"]


class AlunoListSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa_url = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="url",
    )

    class Meta:
        model = Aluno
        fields = ["nome", "email", "id", "capa_url", "capa_attachment_key"]
        capa = AlunoImageSerializer
