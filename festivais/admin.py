from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Genero, Banda, Festival

@admin.register(Banda)
class BandaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'genero')
    list_filter = ('genero',)

@admin.register(Festival)
class FestivalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'localizacao')
    filter_horizontal = ('bandas',)
    search_fields = ('nome',)

admin.site.register(Genero)