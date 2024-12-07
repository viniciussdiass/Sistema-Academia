from django.contrib import admin
from .models import PlanoTreino, Aluno

@admin.register(PlanoTreino)
class PlanoTreinoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor_mensal')
    search_fields = ('nome',)


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'email', 'plano')
    search_fields = ('nome', 'email')
    list_filter = ('plano',)
