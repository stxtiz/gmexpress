from django import forms
import datetime
from django.core.exceptions import ValidationError
from stdnum.cl import rut as rut_utils
import re

from usuarios.choices import estado
from usuarios.models import TipoUsuario, Usuario

class TipoUsuarioForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Descripción'}))
    estado = forms.ChoiceField(choices=estado, widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = TipoUsuario
        fields = ['descripcion', 'estado']
    
    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if not descripcion:
            raise forms.ValidationError("La descripción es requerida.")
        
        # Patrón de expresión regular para permitir solo letras, números, espacios y tildes.
        pattern = re.compile(r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑüÜ\s]+$')
        
        if not pattern.fullmatch(descripcion):
            raise forms.ValidationError("La descripción solo debe contener letras, números, espacios y tildes.")
        
        return descripcion

class UsuarioForm(forms.ModelForm):
    run = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese RUT'}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Nombre'}))  
    paterno = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Apellido Paterno'}))
    materno = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Apellido Materno'}))
    correo = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Correo Electrónico'}))
    contrasenia = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Contraseña'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Teléfono'}))
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','placeholder': 'Día/Mes/Año','type': 'date'}))
    
    estado = forms.ChoiceField(
        choices=estado,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    tipo_usuario = forms.ModelChoiceField(
        queryset=TipoUsuario.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Seleccione Tipo de Usuario"
    )
    
    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data['fecha_nacimiento']
        #rango permitido
        fecha_minima = datetime.date(1900, 1, 1)
        fecha_maxima = datetime.date(2006, 12, 31)
        
        if fecha_nacimiento < fecha_minima or fecha_nacimiento > fecha_maxima:
            raise ValidationError(f'La fecha de nacimiento debe estar entre {fecha_minima} y {fecha_maxima}.')

        return fecha_nacimiento

    def clean_run(self):
        run = self.cleaned_data['run']
        run_compacto = rut_utils.compact(run)

        if not rut_utils.is_valid(run_compacto):
            raise ValidationError('Ingrese un RUT válido (ejemplo: 12345678-5).')

        # Devuelve el RUT formateado de manera estándar
        run_formateado = rut_utils.format(run_compacto)
        
        # Verificar si el RUT ya existe (excluyendo el usuario actual si está editando)
        usuarios_existentes = Usuario.objects.filter(run=run_formateado)
        if self.instance.pk:  # Si estamos editando
            usuarios_existentes = usuarios_existentes.exclude(pk=self.instance.pk)
        
        if usuarios_existentes.exists():
            raise ValidationError('Ya existe un usuario registrado con este RUT.')
        
        return run_formateado

    def clean_correo(self):
        correo = self.cleaned_data['correo']
        
        # Verificar si el correo ya existe (excluyendo el usuario actual si está editando)
        usuarios_existentes = Usuario.objects.filter(correo=correo)
        if self.instance.pk:  # Si estamos editando
            usuarios_existentes = usuarios_existentes.exclude(pk=self.instance.pk)
        
        if usuarios_existentes.exists():
            raise ValidationError('Ya existe un usuario registrado con este correo electrónico.')
        
        return correo
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        # Patrón de expresión regular para permitir solo letras (mayúsculas y minúsculas), espacios y tildes.
        #    ^ ... $  -> La cadena debe empezar y terminar con estos caracteres.
        #    [...]+   -> Al menos un carácter del conjunto.
        #    a-zA-Z  -> Letras de la A a la Z (mayúsculas y minúsculas).
        #    áéíóúÁÉÍÓÚñÑüÜ -> Letras con tildes, ñ y diéresis.
        #    \s       -> Espacios.
        pattern = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$')

        if nombre:
            if not pattern.fullmatch(nombre):
                # Si el 'nombre' NO coincide completamente con el patrón, lanza el error.
                raise forms.ValidationError("El nombre solo debe contener letras, espacios y tildes.")
        
        return nombre

    def clean_paterno(self):
        paterno = self.cleaned_data.get('paterno')
        pattern = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$')

        if paterno:
            if not pattern.fullmatch(paterno):

                raise forms.ValidationError("El apellido paterno solo debe contener letras, espacios y tildes.")

        return paterno

    def clean_materno(self):
        materno = self.cleaned_data.get('materno')
        pattern = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$')

        if materno:
            if not pattern.fullmatch(materno):

                raise forms.ValidationError("El apellido materno solo debe contener letras, espacios y tildes.")

        return materno

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        telefono = telefono.replace(' ', '').strip()

        if not telefono.isdigit():
            raise ValidationError('El teléfono solo debe contener números.')

        if len(telefono) != 9 or telefono[0] not in '23456789':
            raise ValidationError('Ingrese un teléfono chileno válido de 9 dígitos.')

        return telefono

    class Meta:
        model = Usuario
        fields = '__all__'    
    
