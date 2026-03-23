from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Categoria, Produto, Cliente, Pedido, ItemPedido

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'data_pedido')
    inlines = [ItemPedidoInline]

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Cliente)