from django.shortcuts import render, redirect, get_object_or_404
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

#-----------Modulo servicios------------

#Mostrar servicios
def mostrar_servicios(request):
    servicios = Servicio.objects.all()
    
    data = {
        'servicios': servicios
    }
    return render(request, 'templateCatalogue/servicios.html', data)


# Crear SERVICIOS
def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/servicios/')
    else:
        form = ServicioForm()
    return render(request, 'templateCatalogue/servicioAdd.html', {'form': form})

# Cargamos el Servicio para luego modificarlo
def cargar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    form = ServicioForm(instance=servicio)
    return render(request, 'templateCatalogue/servicioEdit.html', {'form': form, 'servicio': servicio})

# Editamos el Servicio
def modificar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    
    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            print("Servicio modificado correctamente.")
            return redirect('/servicios/')
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'templateCatalogue/servicios.html', {'form': form})

#Eliminar Servicio
def eliminar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    
    if request.method == 'POST':
        servicio.delete()
        return redirect('/servicios/')
    return render(request, 'templateCatalogue/servicioEliminar.html', {'servicio': servicio})