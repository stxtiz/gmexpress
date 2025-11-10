from django.shortcuts import render, redirect, get_object_or_404
from catalogue.forms import ProductoForm, ServicioForm, CategoriaForm
from catalogue.models import Producto, Categoria, Servicio
from django.contrib.auth.decorators import permission_required


# Create your views here.


#Productos
@permission_required('catalogue.add_producto')
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mostrarProducto') # <-- SOLUCIÓN: sin 's'
    else:
        form = ProductoForm()
    return render(request, 'templateCatalogue/crear_producto.html', {'form': form})# no olvidar crear la plantilla crear_producto.html

@permission_required('catalogue.view_producto')
def mostrar_producto(request):
    producto = Producto.objects.all()
    categoria = Categoria.objects.all()

    data={
        'producto':producto,
        'categoria':categoria
        
    }   
    return render(request, 'templateCatalogue/productos.html',data)

@permission_required('catalogue.view_producto')
def listar_producto(request):
    return render(request, 'templateCatalogue/productos.html')

@permission_required('catalogue.change_producto')
def cargar_producto(request,id):
    producto = get_object_or_404(Producto,id=id)
    form = ProductoForm(instance=producto)
    return render(request,'templateCatalogue/productoEdit.html',{'form':form,'producto':producto})

@permission_required('catalogue.change_producto')
def modificar_producto(request,id):
    producto = get_object_or_404(Producto,id=id)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            if 'imagen' in request.FILES:
                producto.imagen = request.FILES['imagen']
            form.save()   
        return redirect('mostrarProducto')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'templateCatalogue/productoEdit.html', {'form': form,})

@permission_required('catalogue.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('mostrarProducto')
    return render(request, 'templateCatalogue/eliminarProducto.html', {'producto': producto})


#--------------Categorias------------
# Crear Categoria
@permission_required('catalogue.add_categoria')
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrarCategorias')
    else:
        form = CategoriaForm()
    return render(request, 'templateCatalogue/categoriaAdd.html', {'form': form})

# Mostrar Categorias
@permission_required('catalogue.view_categoria')
def mostrar_categorias(request):
    categorias = Categoria.objects.all()
    data = {
        'categorias': categorias
    }
    return render(request, 'templateCatalogue/categorias.html', data)

# Cargar Categoria para editar
@permission_required('catalogue.change_categoria')
def cargar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    form = CategoriaForm(instance=categoria)
    return render(request, 'templateCatalogue/categoriaEdit.html', {'form': form, 'categoria': categoria})

# Editar Categoria
@permission_required('catalogue.change_categoria')
def modificar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('mostrarCategorias')
        else:
            # Si el formulario no es válido, mostrar errores en la misma página de edición
            print("Errores en el formulario:", form.errors)
            return render(request, 'templateCatalogue/categoriaEdit.html', {'form': form, 'categoria': categoria})
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'templateCatalogue/categoriaEdit.html', {'form': form, 'categoria': categoria})
# Eliminar Categoria
@permission_required('catalogue.delete_categoria')
def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    
    if request.method == 'POST':
        categoria.delete()
        return redirect('mostrarCategorias')
    return render(request, 'templateCatalogue/categoriaEliminar.html', {'categoria': categoria})

#-----------Modulo servicios------------

#Mostrar servicios
@permission_required('catalogue.view_servicio')
def mostrar_servicios(request):
    servicios = Servicio.objects.all()
    
    data = {
        'servicios': servicios
    }
    return render(request, 'templateCatalogue/servicios.html', data)


@permission_required('catalogue.add_servicio')
def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mostrarServicios')
        else:
            # Si el formulario no es válido, mostrar errores
            print("Errores en el formulario:", form.errors)
    else:
        form = ServicioForm()
    return render(request, 'templateCatalogue/servicioAdd.html', {'form': form})

# Cargamos el Servicio para luego modificarlo
@permission_required('catalogue.change_servicio')
def cargar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    form = ServicioForm(instance=servicio)
    return render(request, 'templateCatalogue/servicioEdit.html', {'form': form, 'servicio': servicio})

# Editamos el Servicio
@permission_required('catalogue.change_servicio')
def modificar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    
    if request.method == 'POST':
        form = ServicioForm(request.POST, request.FILES, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('mostrarServicios')
        else:
            # Si el formulario no es válido, mostrar errores en la misma página de edición
            print("Errores en el formulario:", form.errors)
            return render(request, 'templateCatalogue/servicioEdit.html', {'form': form, 'servicio': servicio})
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'templateCatalogue/servicioEdit.html', {'form': form, 'servicio': servicio})

#Eliminar Servicio
@permission_required('catalogue.delete_servicio')
def eliminar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    
    if request.method == 'POST':
        servicio.delete()
        return redirect('mostrarServicios')
    return render(request, 'templateCatalogue/servicioEliminar.html', {'servicio': servicio})