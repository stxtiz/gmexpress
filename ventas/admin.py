from django.contrib import admin
from .models import Venta, DetalleVenta
# Register your models here.


class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion', 'cantidad_items', 'monto_total', 'fecha_venta', '__str__']
    
    
class VentaAdmin(admin.ModelAdmin):
    list_display = ['id', 'num_venta', 'estado', 'tipo_venta', 'detalleVenta', '__str__']
    
    
admin.site.register(DetalleVenta, DetalleVentaAdmin)
admin.site.register(Venta, VentaAdmin)