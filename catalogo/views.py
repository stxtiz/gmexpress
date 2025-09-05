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