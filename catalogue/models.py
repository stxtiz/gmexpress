from django.db import models
from django.utils import timezone
from usuarios.models import Usuario
from catalogue.choices import estado

# modelos de la base de datos: tabla producto - servicio - categoria
class servicio(models.Model):
    idventa = models.AutoField(primary_key=True)
    fechaSolicitud = models.DateTimeField(default=timezone.now)
    estado = models.IntegerField(choices=estado)
    cantidad = models.PositiveIntegerField(null=False, verbose_name="Cantidad")
    producto_idproducto = models.ForeignKey('catalogue.producto', models.DO_NOTHING, db_column='producto_idproducto')
    servicio_idservicio = models.ForeignKey('catalogue.servicio', models.DO_NOTHING, db_column='servicio_idservicio')
    usuario_idusuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    def __str__(self):
        return f"{self.fechaSolicitud} - {self.estado} - {self.cantidad} - {self.producto_idproducto} - {self.servicio_idservicio} - {self.usuario_idusuario}"

    class Meta:
        db_table = 'servicio'
        verbose_name ='servicio'
        verbose_name_plural = 'servicios'

class producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.PositiveIntegerField(null=False, verbose_name="Precio")
    stock = models.PositiveIntegerField(null=False, verbose_name="Stock")
    imagen = models.CharField(max_length=255)
    categoria_idcategoria = models.ForeignKey('catalogue.categoria', models.DO_NOTHING, db_column='categoria_idcategoria')
    def __str__(self):
        return f"{self.nombre} - {self.descripcion} - {self.precio} - {self.stock} - {self.imagen} - {self.categoria_idcategoria}"

    class Meta:
        db_table = 'producto'
        verbose_name ='producto'
        verbose_name_plural = 'productos'

class categoria(models.Model):
    idcategoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    estado = models.PositiveIntegerField(null=False, verbose_name="Estado", choices=estado)
    descripcion = models.CharField(max_length=200, null=False)

    def __str__(self):
        return f"{self.nombre} - {self.descripcion} - {self.estado}"

    class Meta:
        db_table = 'categoria'
        verbose_name ='categoria'
        verbose_name_plural = 'categorias'