# from core.views import turma
# from django_filters import CharFilter, FilterSet
from rest_framework.viewsets import ModelViewSet

from core.models import Aluno
from core.serializers import AlunoSerializer
from core.serializers.aluno import AlunoInfoSerializer, AlunoListSerializer

# class AlunoFilter(FilterSet):
#     turma = CharFilter(field_name="turma__descricao", lookup_expr="contains")

#     class Meta:
#         model = Aluno
#         fields = ["turma"]


class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return AlunoListSerializer
        elif self.action == "retrieve":
            return AlunoInfoSerializer
        return AlunoSerializer
