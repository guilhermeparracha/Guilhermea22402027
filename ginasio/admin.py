from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PT, Membro, Sessao

admin.site.register(PT)
admin.site.register(Membro)

@admin.register(Sessao)
class SessaoAdmin(admin.ModelAdmin):
    list_display = ('pt', 'membro', 'data', 'hora')
    list_filter = ('data', 'pt')
    date_hierarchy = 'data' 