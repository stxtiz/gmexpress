from django.db import models
from django.utils import timezone

# modelos de la base de datos: tabla producto - servicio - categoria
class servicio(models.Model):
    idventa = models.AutoField(primary_key=True)
    fechaSolicitud = models.DateTimeField(default=timezone.now)
    estado = models.IntegerField(max_length=50)
    cantidad = models.IntegerField()
    producto_idproducto = models.ForeignKey('catalogue.producto', models.DO_NOTHING, db_column='producto_idproducto')
    servicio_idservicio = models.ForeignKey('catalogue.servicio', models.DO_NOTHING, db_column='servicio_idservicio')
    usuario_idusuario = models.ForeignKey('users.usuario', models.DO_NOTHING, db_column='usuario_idusuario')
    def __str__(self):
        return f"{self.idventa} - {self.fechaSolicitud} - {self.estado} - {self.cantidad} - {self.producto_idproducto} - {self.servicio_idservicio} - {self.usuario_idusuario}"

    class Meta:
        db_table = 'servicio'
        verbose_name ='servicio'
        verbose_name_plural = 'servicios'

class producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.CharField(max_length=50)
    stock = models.IntegerField()
    imagen = models.CharField(max_length=255)
    categoria_idcategoria = models.ForeignKey('catalogue.categoria', models.DO_NOTHING, db_column='categoria_idcategoria')
    def __str__(self):
        return f"{self.idproducto} - {self.nombre} - {self.descripcion} - {self.precio} - {self.stock} - {self.imagen} - {self.categoria_idcategoria}"

    class Meta:
        db_table = 'producto'
        verbose_name ='producto'
        verbose_name_plural = 'productos'

class categoria(models.Model):
    idcategoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.idcategoria} - {self.nombre}"

    class Meta:
        db_table = 'categoria'
        verbose_name ='categoria'
        verbose_name_plural = 'categorias'