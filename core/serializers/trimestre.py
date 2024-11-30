from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import Trimestre


class TrimestreSerializer(ModelSerializer):
    ano = serializers.IntegerField(source="ano.data")

    class Meta:
        model = Trimestre
        fields = "__all__"
