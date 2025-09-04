from django.http import HttpResponse

from django.shortcuts import render

def info_empresa(request): 
    datos = {
        'historia': "GM Express es líder en servicios gastronómicos...",
        'mision': "Brindar alimentación de calidad...",
        'vision': "Consolidarnos como una empresa de alimentación sostenible y de excelencia en la región, reconocida por superar y entregar la mejor experiencia a sus clientes, con productos y servicios de alta calidad y confiabilidad.",
        'valores': ["Compromiso", "Calidad", "Innovación", "Trabajo en equipo"],
        'contactos': {
            'teléfono': "+56912345678",
            'email': "ventas@gmexpress.cl"
        },
        'redes': [
            {'nombre': "Facebook", 'url': "https://facebook.com/gmexpress"},
            {'nombre': "Instagram", 'url': "https://instagram.com/gmexpress"},
        ]
    }
    # Comentario: renderiza la plantilla y pasa el diccionario 'datos'
    return render(request, 'templateEmpresa/info.html', datos)

def inicio(request):
    return render(request, 'templateEmpresa/inicio.html')