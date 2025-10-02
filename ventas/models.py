from django.db import models
from django.utils import timezone
from ventas.choices import estado, tipo_venta
# Create your models here.



class DetalleVenta(models.Model):
    descripcion = models.CharField(max_length=100, null=False)
    cantidad_items = models.IntegerField(null=False)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    fecha_venta = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "detalle_ventas"
        verbose_name = "Detalle Venta"
        verbose_name_plural = "Detalles Ventas"
        
    def __str__(self):
        return f" {self.cantidad_items} - {self.descripcion} - {self.fecha_venta} - {self.monto_total}"
    
    
class Venta(models.Model):
    num_venta = models.CharField(max_length=45, unique=True, null=False)
    estado = models.CharField(max_length=1, choices=estado, default='1')
    tipo_venta = models.CharField(max_length=1, choices=tipo_venta, default='1')
    detalleVenta = models.ForeignKey(DetalleVenta, on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table = "ventas"
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        
    def __str__(self):
        return f" {self.num_venta} - {self.estado} - {self.tipo_venta} "