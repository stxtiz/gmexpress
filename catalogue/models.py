from django.db import models
from django.utils import timezone
from catalogue.choices import estado
import os

# modelos de la base de datos: tabla producto - servicio - categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    estado = models.CharField(max_length=1,choices=estado,default='1', verbose_name="Estado")
    descripcion = models.CharField(max_length=200, null=False)

    def __str__(self):
        return f"CATEGORÍA: {self.nombre}"

    class Meta:
        db_table = 'categoria'
        verbose_name ='Categoria'
        verbose_name_plural = 'Categorias'
        
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.PositiveIntegerField(null=False, verbose_name="Precio")
    stock = models.PositiveIntegerField(null=False, verbose_name="Stock")
    
    imagen = models.CharField(max_length=255, default='default.jpg')# revision para despues cambiar a ImageField
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, limit_choices_to={'estado': '1'}, verbose_name="Categoría", blank=True, null=True)
    def __str__(self):
        return f"ID: {self.id} | NOMBRE: {self.nombre} | DESCRIPCIÓN: {self.descripcion} | PRECIO: {self.precio} | STOCK: {self.stock} | IMAGEN: {self.imagen} | CATEGORÍA: {self.categoria}"

    class Meta:
        db_table = 'producto'
        verbose_name ='Producto'
        verbose_name_plural = 'Productos'




class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.PositiveIntegerField(null=False, verbose_name="Precio")
    estado = models.CharField(max_length=1,choices=estado,default='1', verbose_name="Estado")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    
    def generarNombreArchivo(instance, filename):
        extension = os.path.splitext(filename)[1][1:]
        ruta = 'servicios'
        fecha = timezone.now().strftime('%d%m%Y_%H%M%S')
        nombre_archivo = "{}.{}".format(fecha, extension)
        return os.path.join(ruta, nombre_archivo)
    imagen = models.ImageField(upload_to=generarNombreArchivo, default='servicios/default.jpg')

    def __str__(self):
        return f"ID: {self.id} | NOMBRE: {self.nombre} | DESCRIPCIÓN: {self.descripcion} | PRECIO: {self.precio} | ESTADO: {self.estado} | FECHA DE CREACIÓN: {self.fecha_creacion}"

    class Meta:
        db_table = 'servicio'
        verbose_name ='Servicio'
        verbose_name_plural = 'Servicios'


