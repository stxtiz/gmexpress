from django.db import models
from django.utils import timezone

# Create your models here.

class TipoUsuario(models.Model):
    descripcion = models.CharField(max_length=45)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name = "Tipo Usuario"
        verbose_name_plural = "Tipos Usuarios"
        
    def __str__(self):
        return f"{self.descripcion}"
        
class Usuario(models.Model):
    nombre = models.CharField(max_length=45, null=False)
    apellido = models.CharField(max_length=45, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    contrasenia_hash = models.CharField(max_length=255, null=False)
    telefono = models.CharField(max_length=15, blank=True, null=False)
    fecha_nacimiento = models.DateField(blank=True, null=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.email}"
    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"