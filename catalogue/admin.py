
from django.contrib import admin
from .models import producto, categoria, servicio
# Register your models here.

class categoriaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nombre',
        'estado',
        'descripcion',
    ]
    




class productoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nombre',
        'descripcion',
        'precio',
        'stock',
        'imagen',
        'categoria_id',
    ]


class servicioAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'fechaSolicitud',
        'estado',
        'cantidad',
    ]
admin.site.register(producto, productoAdmin)
admin.site.register(categoria, categoriaAdmin)
admin.site.register(servicio, servicioAdmin)
