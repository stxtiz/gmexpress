from django import forms
from catalogue.choices import estado
from catalogue.models import Categoria, Producto

def clean_precio(self):
    precio = self.cleaned_data['precio']
    try:
        precio = int(precio)
    except ValueError:
        raise forms.ValidationError("El precio debe ser un número entero.")
    
    if precio <= 0:
        raise forms.ValidationError("El precio debe ser mayor a cero.")
    return precio

def clean_stock(self):
    stock = self.cleaned_data['stock']
    try:
        stock = int(stock)
    except ValueError:
        raise forms.ValidationError("El stock debe ser un número entero.")
    if stock < 0:
        raise forms.ValidationError("El stock no puede ser negativo.")
    return stock

def clean_nombre(self):
    nombre = self.cleaned_data.get('nombre')
    if nombre and not nombre.isalpha() and ' ' not in nombre:
        raise forms.ValidationError("El nombre solo debe contener letras.")

def clean_descripcion(self):
    descripcion = self.cleaned_data.get('descripcion')
    try:
        descripcion = str(descripcion)
    except ValueError:
        raise forms.ValidationError("La descripción debe ser una cadena de texto.")
    return descripcion





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