"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from black import mode

from core import models
from core.models.turma import Turma


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ["id"]
    list_display = ["email", "name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("name", "passage_id")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
        (_("Groups"), {"fields": ("groups",)}),
        (_("User Permissions"), {"fields": ("user_permissions",)}),
    )
    readonly_fields = ["last_login"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "turma__nome", "matricula")
    search_fields = ("nome", "matricula", "turma__nome")
    list_filter = ("turma", "nome")
    ordering = ("nome", "turma__nome", "matricula")
    list_per_page = 25


@admin.register(models.Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ("nome", "curso__nome", "ano__data")
    search_fields = ("nome", "curso__nome")
    list_filter = ("ano", "curso")
    ordering = ("nome", "curso__nome", "ano__data")
    list_per_page = 21


# @admin.register(models.Ocorrencia)
# class OcorrenciaAdmin(admin.ModelAdmin):
#     list_display = ("aluno")
#     search_fields = ()
#     list_filter = ()
#     ordering = ()
#     list_per_page = 10


@admin.register(models.Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ("valor", "disciplina", "trimestre")
    search_fields = ("valor", "disciplina", "trimestre")
    list_filter = ("valor", "trimestre")
    ordering = ("valor", "disciplina", "trimestre")
    list_per_page = 10


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Disciplina)
admin.site.register(models.Curso)
admin.site.register(models.Ano)
admin.site.register(models.Ocorrencia)
admin.site.register(models.Professor)
admin.site.register(models.Trimestre)
