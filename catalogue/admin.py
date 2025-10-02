
from django.contrib import admin
from .models import producto, categoria, servicio
# Register your models here.

class productoAdmin(admin.ModelAdmin):
    list_display = [
        'idproducto',
        'nombre',
        'descripcion',
        'precio',
        'stock',
        'imagen',
        'categoria_idcategoria',
        '__str__'
    ]


admin.site.register(producto, productoAdmin)

