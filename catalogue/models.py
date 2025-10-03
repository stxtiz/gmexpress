from django.db import models
from django.utils import timezone
from usuarios.models import Usuario
from catalogue.choices import estado

# modelos de la base de datos: tabla producto - servicio - categoria
class categoria(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    estado = models.CharField(max_length=1,choices=estado,default='1', verbose_name="Estado")
    descripcion = models.CharField(max_length=200, null=False)

    def __str__(self):
        return f"ID: {self.id} | NOMBRE: {self.nombre} | DESCRIPCIÓN: {self.descripcion} | ESTADO: {self.estado}"

    class Meta:
        db_table = 'categoria'
        verbose_name ='Categoria'
        verbose_name_plural = 'Categorias'
        
class producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.PositiveIntegerField(null=False, verbose_name="Precio")
    stock = models.PositiveIntegerField(null=False, verbose_name="Stock")
    imagen = models.CharField(max_length=255)
    categoria_id = models.ForeignKey(categoria, on_delete=models.PROTECT, verbose_name="Categoría")
    def __str__(self):
        return f"ID: {self.id} | NOMBRE: {self.nombre} | DESCRIPCIÓN: {self.descripcion} | PRECIO: {self.precio} | STOCK: {self.stock} | IMAGEN: {self.imagen} | CATEGORÍA: {self.categoria_id}"

    class Meta:
        db_table = 'producto'
        verbose_name ='Producto'
        verbose_name_plural = 'Productos'

class servicio(models.Model):
    fechaSolicitud = models.DateField(default=timezone.now, verbose_name="Fecha de Solicitud")
    estado = models.CharField(max_length=1,choices=estado,default='1', verbose_name="Estado")
    cantidad = models.PositiveIntegerField(null=False, verbose_name="Cantidad")
    def __str__(self):
        return f"SERVICIO: {self.id} | FECHA: {self.fechaSolicitud} | ESTADO: {self.estado} | CANTIDAD: {self.cantidad}"

    class Meta:
        db_table = 'servicio'
        verbose_name ='Servicio'
        verbose_name_plural = 'Servicios'


