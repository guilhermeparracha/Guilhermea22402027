from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Ingrediente, Receita

admin.site.register(Ingrediente)

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    filter_horizontal = ('ingredientes', 'favoritada_por') 