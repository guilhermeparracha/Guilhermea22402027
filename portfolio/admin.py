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