
from django.contrib import admin
from .models import Producto, Categoria
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nombre',
        'estado',
        'descripcion',
    ]
    




class ProductoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nombre',
        'descripcion',
        'precio',
        'stock',
        'imagen',
        'categoria_id',
    ]

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
