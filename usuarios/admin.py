from django.contrib import admin
from .models import TipoUsuario, Usuario
# Register your models here.
class TipoUsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion', 'activo', 'fecha_creacion']

class UsuarioAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nombre',
        'apellido',
        'email',
        'telefono',
        'fecha_nacimiento',
        'fecha_registro',
        'activo',
        'tipo_usuario',
        'nombre_completo'
    ]


admin.site.register(TipoUsuario, TipoUsuarioAdmin)
admin.site.register(Usuario, UsuarioAdmin)