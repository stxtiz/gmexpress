from django import forms
from catalogue.choices import estado
from catalogue.models import Categoria, Producto, Servicio


#Validaciones para el formulario de Servicios
#validacion precio
def clean_precio(self):
    precio = self.cleaned_data['precio']
    try:
        precio = int(precio)
    except ValueError:
        raise forms.ValidationError("El precio debe ser un número entero.")
    if precio < 0:
        raise forms.ValidationError("El precio no puede ser negativo.")
    return precio
#validacion nombre
def clean_nombre(self):
    nombre = self.cleaned_data['nombre']
    if nombre and not nombre.isalpha() and ' ' not in nombre:
        raise forms.ValidationError("El nombre solo debe contener letras y espacios.")
    return nombre
#validacion descripcion
def clean_descripcion(self):
    descripcion = self.cleaned_data['descripcion']
    if descripcion and not descripcion.isalpha() and ' ' not in descripcion:
        raise forms.ValidationError("La descripción solo debe contener letras y espacios.")
#Formulario para el modelo Servicio
class ServicioForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Nombre del servicio'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Descripción del servicio'}))
    precio = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Precio del servicio'}))
    estado = forms.CharField(widget=forms.Select(choices=estado, attrs={'class': 'form-select'}))

    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion','precio', 'estado']
        
        

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese el nombre del producto'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese la descripción del producto'}))
    precio = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Ingrese el precio del producto'}))
    stock = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Ingrese el stock del producto'}))

    imagen = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),required=False)# despues cambiar 
    #no c si el producto debe llevar estado ya que en la base  en los models no lo tiene
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),        
        empty_label="Seleccione una categoría",
        widget=forms.Select(attrs={'class': 'form-control'}),required=False# cambiar 
    )
    class Meta:
        model = Producto
        fields = '__all__'