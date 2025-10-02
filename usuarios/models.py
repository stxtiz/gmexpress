from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from usuarios.choices import estado

# Create your models here.

class TipoUsuario(models.Model):
    descripcion = models.CharField(max_length=45)
    estado = models.CharField(max_length=1, choices=estado, default='1')
    fecha_creacion = models.DateTimeField(default=timezone.now)
        
    def __str__(self):
        return f"{self.descripcion}"
    
    class Meta:
        db_table = 'tipo_usuario'
        verbose_name = "Tipo Usuario"
        verbose_name_plural = "tipos Usuarios"
        
class Usuario(models.Model):
    run = models.CharField(max_length=12, unique=True, null=False)
    nombre = models.CharField(max_length=45, null=False, blank=False)
    paterno = models.CharField(max_length=45, null=False, blank=False)
    materno = models.CharField(max_length=45, null=False, blank=False)
    correo = models.EmailField(max_length=100, unique=True, null=False)
    contrasenia = models.CharField(max_length=255, validators=[RegexValidator(r'^(?=.*[A-Z])(?=.*[^A-Za-z0-9]).{9,}$', message="Debe tener al menos 9 caracteres, una mayúscula y un símbolo especial.")])
    telefono = models.CharField(max_length=15, null=False, blank=False)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    fecha_registro = models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=1,choices=estado,default='1')
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.PROTECT)
    
    class Meta:
        db_table = 'usuario'
        verbose_name = "Usuario"
        verbose_name_plural = "usuarios"
        
    def __str__(self):
        return f"{self.nombre} {self.paterno} {self.materno} - {self.correo}"
    
    def nombre_completo(self):
        return f"{self.nombre} {self.paterno} {self.materno}"