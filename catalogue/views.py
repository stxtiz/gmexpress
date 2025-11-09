from django.shortcuts import render, redirect
from catalogue.forms import ServicioForm
from catalogue.models import Servicio
# Create your views here.

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
            return redirect('templateCatalogue/servicios.html')
    else:
        form = ServicioForm()
    return render(request, 'templateCatalogue/servicioAdd.html', {'form': form})
