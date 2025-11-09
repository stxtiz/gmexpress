from django.shortcuts import render,redirect
from catalogue.forms import ProductoForm
from catalogue.models import Producto, Categoria


# Create your views here.
def productos(request):
    return render(request, 'templateCatalogue/productos.html')

#Productos

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request, 'templateCatalogue/productos.html')
    else:
        form = ProductoForm()
    return render(request, 'templateCatalogue/crear_producto.html', {'form': form})# no olvidar crear la plantilla crear_producto.html