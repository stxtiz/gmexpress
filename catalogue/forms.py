from django import forms
from catalogue.choices import estado
from catalogue.models import Categoria, Producto

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