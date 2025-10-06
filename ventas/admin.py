from django.contrib import admin
from .models import Venta, DetalleVenta
# Register your models here.
class VentaAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha_venta', 'tipo_venta', 'monto_total', 'estado', 'usuario']
    
    
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ['id', 'venta', 'producto', 'precio_unitario', 'cantidad' , 'calcular_subtotal_producto']
    
    
admin.site.register(Venta, VentaAdmin)
admin.site.register(DetalleVenta, DetalleVentaAdmin)