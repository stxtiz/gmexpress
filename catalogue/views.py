from django.shortcuts import render,redirect
from catalogue.forms import ProductoForm, ServicioForm
from catalogue.models import Producto, Categoria, Servicio


# Create your views here.
def productos(request):
    return render(request, 'templateCatalogue/productos.html')

#Productos

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('templateCatalogue/productos.html')
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

#modulo servicios

def mostrar_servicios(request):
    servicios = Servicio.objects.all()
    
    data = {
        'servicios': servicios
    }
    return render(request, 'templateCatalogue/servicios.html', data)



def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('templateCatalogue/servicios.html')
    else:
        form = ServicioForm()
    return render(request, 'templateCatalogue/servicioAdd.html', {'form': form})

