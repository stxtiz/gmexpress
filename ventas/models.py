from django.db import models
from django.utils import timezone
from ventas.choices import estado, tipo_venta
# Create your models here.

class Venta(models.Model):
    num_venta = models.CharField(max_length=45, unique=True, null=False)
    cantidad_items = models.IntegerField(null=False)
    descripcion = models.CharField(max_length=100, null=False)
    fecha_venta = models.DateTimeField(default=timezone.now)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    estado = models.CharField(max_length=1, choices=estado, default='1')
    tipo_venta = models.CharField(max_length=1, choices=tipo_venta, default='1')
    
    
    class Meta:
        db_table = "ventas"
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        
    def __str__(self):
        return f" {self.num_venta} - {self.cantidad_items} - {self.descripcion} - {self.fecha_venta} - {self.monto_total} - {self.estado} - {self.tipo_venta}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto_servicio = models.CharField(max_length=100, null=False)
    cantidad = models.IntegerField(null=False)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    
    class Meta:
        db_table = "detalle_ventas"
        verbose_name = "Detalle Venta"
        verbose_name_plural = "Detalles Ventas"
        
    def __str__(self):
        return f" {self.venta.num_venta} - {self.producto_servicio} - {self.cantidad} - {self.precio_unitario} - {self.subtotal}"