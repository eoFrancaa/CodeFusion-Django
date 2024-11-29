from rest_framework.serializers import ModelSerializer

from core.models import Ano


class AnoSerializer(ModelSerializer):
    class Meta:
        model = Ano
        field = "__all__"
