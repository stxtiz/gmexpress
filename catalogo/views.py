from django.shortcuts import render
from catalogo import models as datos
# Create your views here.
def catalogoServicios(request):
    data = {
        'catalogo_servicios': datos.catalogo1,
    }
    return render(request, 'templateCatalogo/catalogo1.html', data)

def catalogoTransporte(request):
    data = {
        'catalogo_transporte': datos.catalogo_transportado,
    }
    return render(request, 'templateCatalogo/transporte.html', data)

def catalogoCoffe(request):
    data = {
        'catalogo_coffe': datos.catalogo_coffee,
    }
    return render(request, 'templateCatalogo/coffe.html', data)

def catalogoReposteria(request):
    data = {
        'catalogo_reposteria': datos.catalogo_reposteria,
    }
    return render(request, 'templateCatalogo/reposteria.html', data)

def catalogoTradicional(request):
    data = {
        'catalogo_tradicional': datos.catalogo_tradicional,
    }
    return render(request, 'templateCatalogo/tradicional.html', data)

def catalogoConcesion(request):
    data = {
        'catalogo_concesion': datos.catalogo_concesion,
    }
    return render(request, 'templateCatalogo/concesion.html', data)

def menuTransportado(request):
    data = {
        'menu_items': datos.menu_transportado,
        'titulo': 'Menú Transportado'
    }
    return render(request, 'templateCatalogo/menu_detail.html', data)

def menuCoffe(request):
    data = {
        'menu_items': datos.menu_coffe,
        'titulo': 'Menú Coffee Break'
    }
    return render(request, 'templateCatalogo/menu_detail.html', data)

def menuReposteria(request):
    data = {
        'menu_items': datos.menu_reposteria,
        'titulo': 'Menú Repostería'
    }
    return render(request, 'templateCatalogo/menu_detail.html', data)

def menuEspecial(request):
    data = {
        'menu_items': datos.menu_especial,
        'titulo': 'Menú Especial'
    }
    return render(request, 'templateCatalogo/menu_detail.html', data)

def menuConcesion(request):
    data = {
        'menu_items': datos.menu_concesion,
        'titulo': 'Personal de Concesión'
    }
    return render(request, 'templateCatalogo/menu_detail.html', data)