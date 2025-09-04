from django.shortcuts import render
from catalogo import models as datos
# Create your views here.
def catalogoServicios(request):
    data = {
        'catalogo_servicios': datos.catalogo1
    }
    return render(request, 'templateCatalogo/catalogo1.html', data)