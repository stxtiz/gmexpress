from django import forms
from usuarios.choices import estado
from usuarios.models import TipoUsuario, Usuario

class TipoUsuarioForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Descripción'}))
    estado = forms.ChoiceField(choices=estado, widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = TipoUsuario
        fields = '__all__'

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

    class Meta:
        model = Usuario
        fields = '__all__'    
    
