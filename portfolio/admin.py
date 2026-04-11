from django.contrib import admin
from .models import Licenciatura, UnidadeCurricular, Tecnologia, Projeto, TFC, Formacao, Competencia, MakingOf

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'grau', 'ects')
    search_fields = ('nome',)

@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre', 'ects')
    list_filter = ('ano', 'semestre')
    search_fields = ('nome',)
    filter_horizontal = ('licenciaturas',)

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel_interesse')
    search_fields = ('nome',)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'uc')
    list_filter = ('uc',)
    search_fields = ('titulo', 'descricao')
    filter_horizontal = ('tecnologias',)

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'ano')
    list_filter = ('ano',)
    search_fields = ('titulo', 'autor')

@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'instituicao', 'data_inicio', 'licenciatura')
    list_filter = ('instituicao', 'licenciatura')

@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria')
    filter_horizontal = ('projetos',)

@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ('titulo_etapa', 'data')
    readonly_fields = ('data',)