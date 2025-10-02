from django.contrib import admin
from .models import TipoUsuario, Usuario
# Register your models here.
class TipoUsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion', 'estado', 'fecha_creacion']

class UsuarioAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'run',
        'nombre',
        'paterno',
        'materno',
        'correo',
        'telefono',
        'fecha_nacimiento',
        'fecha_registro',
        'estado',
        'tipo_usuario',
        'nombre_completo'
    ]


admin.site.register(TipoUsuario, TipoUsuarioAdmin)
admin.site.register(Usuario, UsuarioAdmin)