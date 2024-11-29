from rest_framework.viewsets import ModelViewSet

from core.models import Professor
from core.serializers import ProfessorSerializer
from core.serializers.professor import ProfessorInfoSerializer, ProfessorListSerializer


class ProfessorViewSet(ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ProfessorListSerializer
        elif self.action == "retrieve":
            return ProfessorInfoSerializer
        return ProfessorSerializer
