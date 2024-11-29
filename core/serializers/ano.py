from rest_framework.serializers import ModelSerializer

from core.models import Ano


class AnoSerializer(ModelSerializer):
    class Meta:
        model = Ano
        fields = "__all__"
