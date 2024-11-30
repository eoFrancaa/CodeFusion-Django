from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views import (
    AlunoViewSet,
    CursoViewSet,
    DisciplinaViewSet,
    NotaViewSet,
    OcorrenciaViewSet,
    ProfessorViewSet,
    TurmaViewSet,
    UserViewSet,
)
from uploader.router import router as uploader_router

router = DefaultRouter()

router.register(r"usuarios", UserViewSet, basename="usuarios")
router.register(r"disciplinas", DisciplinaViewSet, basename="disciplinas")
router.register(r"cursos", CursoViewSet, basename="cursos")
router.register(r"turmas", TurmaViewSet, basename="turmas")
router.register(r"alunos", AlunoViewSet, basename="alunos")
router.register(r"ocorrências", OcorrenciaViewSet, basename="ocorrências")
router.register(r"professores", ProfessorViewSet, basename="professores")
router.register(r"notas", NotaViewSet, basename="notas")
router.registry.extend(uploader_router.registry)

urlpatterns = [
    path("admin/", admin.site.urls),
    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    # API
    path("api/", include(router.urls)),
    path("api/media/", include(uploader_router.urls)),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
