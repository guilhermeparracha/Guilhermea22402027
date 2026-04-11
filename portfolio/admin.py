from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Licenciatura

admin.site.register(Licenciatura)

from django.contrib import admin
from .models import Licenciatura, UnidadeCurricular

@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre', 'ects')
    list_filter = ('ano', 'licenciaturas')
    search_fields = ('nome',)
    filter_horizontal = ('licenciaturas',)

from .models import Tecnologia, Projeto

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel_interesse')

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'uc')
    filter_horizontal = ('tecnologias',) 