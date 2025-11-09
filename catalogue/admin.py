
from django.contrib import admin
from .models import Producto, Categoria, Servicio
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

class ServicioAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nombre',
        'descripcion',
        'precio',
        'estado'
        
    ]

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Servicio, ServicioAdmin)
