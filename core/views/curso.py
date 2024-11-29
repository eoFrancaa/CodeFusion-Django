from rest_framework.viewsets import ModelViewSet

from core.models import Curso
from core.serializers import CursoSerializer
from core.serializers.curso import CursoListSerializer


class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    pagination_class = None

    def get_serializer_class(self):
        if self.action == "list":
            return CursoListSerializer
        elif self.action == "retrieve":
            return CursoSerializer
