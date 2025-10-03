from django.db import models
from django.utils import timezone
from ventas.choices import estado, tipo_venta
# Create your models here.



class DetalleVenta(models.Model):
    descripcion = models.CharField(max_length=100, null=False, verbose_name="Descripción")
    cantidad_items = models.PositiveIntegerField(null=False, verbose_name="Cantidad de Ítems")
    monto_total = models.PositiveIntegerField(max_length=100, null=False, verbose_name="Monto Total")
    fecha_venta = models.DateField(default=timezone.now, verbose_name="Fecha de Venta")

    class Meta:
        db_table = "detalle_ventas"
        verbose_name = "Detalle Venta"
        verbose_name_plural = "Detalles Ventas"
        
    def __str__(self):
        return f" ID: {self.id} | CANTIDAD DE ITEMS: {self.cantidad_items} | FECHA: {self.fecha_venta} | MONTO TOTAL: {self.monto_total}"
    
    
class Venta(models.Model):
    num_venta = models.PositiveIntegerField(unique=True, null=False, verbose_name="Número de Venta")
    estado = models.CharField(max_length=1, choices=estado, default='1', verbose_name="Estado")
    tipo_venta = models.CharField(max_length=1, choices=tipo_venta, default='p', verbose_name="Tipo de Venta")
    detalleVenta = models.ForeignKey(DetalleVenta, on_delete=models.CASCADE, null=True, verbose_name="Detalle de Venta")
    
    class Meta:
        db_table = "ventas"
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        
