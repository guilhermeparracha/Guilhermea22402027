from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Turma, Professor, Aluno

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'turma')
    list_filter = ('turma',)

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'turma')
    search_fields = ('nome',)
    list_filter = ('turma',)