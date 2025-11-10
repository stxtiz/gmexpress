from django import forms
from catalogue.choices import estado
from catalogue.models import Categoria, Producto, Servicio
import re  # Importa el módulo de expresiones regulares


#Validaciones 

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
    
    
    
#-------------------Formulario para el modelo Servicio----------------------------------
class ServicioForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Nombre del servicio'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Descripción del servicio'}))
    precio = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Precio del servicio'}),
        min_value=0,
        max_value=2147483647  
    )
    estado = forms.CharField(widget=forms.Select(choices=estado, attrs={'class': 'form-select'}))
    imagen = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion','precio', 'estado', 'imagen']
    
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is None:
            raise forms.ValidationError("El precio es requerido.")
        if precio < 0:
            raise forms.ValidationError("El precio no puede ser negativo.")
        if precio > 2147483647:
            raise forms.ValidationError("El precio es demasiado grande. El máximo permitido es 2,147,483,647.")
        return precio

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


    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        
        # Reutilizamos el mismo patrón de regex
        pattern = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$')

        if descripcion:
            if not pattern.fullmatch(descripcion):
                raise forms.ValidationError("La descripción solo debe contener letras, espacios y tildes.")
        
        return descripcion

#------------------Formulario para el modelo Categoria----------------------------------
class CategoriaForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese el nombre de la categoría'}))
    estado = forms.CharField(widget=forms.Select(choices=estado, attrs={'class': 'form-select'}))

    class Meta:
        model = Categoria
        fields = '__all__'
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        # Patrón de expresión regular para permitir solo letras (mayúsculas y minúsculas), espacios y tildes.
        pattern = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$')

        if nombre:
            if not pattern.fullmatch(nombre):
                raise forms.ValidationError("El nombre solo debe contener letras, espacios y tildes.")
        
        return nombre
        
        


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