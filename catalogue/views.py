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


def mostrar_productos(request):
    productos = Producto.objects.all(),
    categoria = Categoria.objects.all()

    data={
        'productos':productos,
        'categoria':categoria
        
    }   
    return render(request, 'templateCatalogue/productos.html',data)

def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('mostrar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'templateCatalogue/editar_producto.html', {'form': form})

def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('mostrar_productos')


#Categorias