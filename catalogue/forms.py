from django import forms
from catalogue.choices import estado
from catalogue.models import Categoria, Producto, Servicio
import re


#Validaciones 

#validacion precio

    
    
    
#-------------------Formulario para el modelo Servicio----------------------------------
class ServicioForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Nombre del servicio'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Descripción del servicio'}))
    precio = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Precio del servicio'}))
    estado = forms.CharField(widget=forms.Select(choices=estado, attrs={'class': 'form-select'}))

    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion','precio', 'estado']
        


#-------------------Formulario para el modelo Producto----------------------------------        

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
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        # Patrón de expresión regular para permitir solo letras (mayúsculas y minúsculas), espacios y tildes.
        pattern = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$')

        if nombre:
            if not pattern.fullmatch(nombre):
                raise forms.ValidationError("El nombre solo debe contener letras, espacios y tildes.")
        
        return nombre
    
    def clean_precio(self):
        precio = self.cleaned_data['precio']
        try:
            precio = int(precio)
        except ValueError:
            raise forms.ValidationError("El precio debe ser un número entero.")
        if precio < 0:
            raise forms.ValidationError("El precio no puede ser negativo.")        
        return precio
    
    def clean_stock(self):
        stock = self.cleaned_data['stock']
        try:
            stock = int(stock)
        except ValueError:
            raise forms.ValidationError("El stock de producto debe ser un número entero.")
        if stock < 0:
            raise forms.ValidationError("El stock de producto no puede ser negativo.")
        return stock
    
    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion']
        pattern = re.compile(r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑüÜ\s.,;:!?()-]+$')
        if descripcion:
            if not pattern.fullmatch(descripcion):
                raise forms.ValidationError("La descripción contiene caracteres no permitidos.")
        return descripcion

    
    
    