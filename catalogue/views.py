from django.shortcuts import render,redirect, get_object_or_404
from catalogue.forms import ProductoForm, ServicioForm
from catalogue.models import Producto, Categoria, Servicio


# Create your views here.
def producto(request):
    return render(request, 'templateCatalogue/productos.html')

#Productos

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrarProducto') # <-- SOLUCIÓN: sin 's'
    else:
        form = ProductoForm()
    return render(request, 'templateCatalogue/crear_producto.html', {'form': form})# no olvidar crear la plantilla crear_producto.html


def mostrar_producto(request):
    producto = Producto.objects.all()
    categoria = Categoria.objects.all()

    data={
        'producto':producto,
        'categoria':categoria
        
    }   
    return render(request, 'templateCatalogue/productos.html',data)

def cargar_producto(request,id):
    producto = get_object_or_404(Producto,id=id)
    form = ProductoForm(instance=producto)
    return render(request,'templateCatalogue/productoEdit.html',{'form':form,'producto':producto})


def modificar_producto(request,id):
    producto = get_object_or_404(Producto,id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST,instance=producto)
        if form.is_valid():
            form.save()   
        return redirect('mostrarProducto')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'templateCatalogue/productoEdit.html', {'form': form,})


def eliminar_producto(request,id):
    producto = get_object_or_404(Producto,id=id)

    if request.method == 'POST':
        producto.delete()
        return redirect('mostrarProducto')
    return render(request,'templateCatalogue/eliminarProducto.html',{'producto':producto})




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
