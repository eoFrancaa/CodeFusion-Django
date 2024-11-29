from rest_framework.viewsets import ModelViewSet

from core.models import Ano
from core.serializers import AnoSerializer


class AnoViewSet(ModelViewSet):
    queryset = Ano.objects.all()
    serializer_class = AnoSerializer
