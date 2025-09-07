from django.shortcuts import render
from catalogo import models as datos
# Create your views here.
def catalogoServicios(request):
    data = {
        'catalogo_servicios': datos.catalogo1,
    }
    return render(request, 'templateEmpresa/inicio.html', data)

def catalogoProductos(request, servicio_tipo):
    # Mapeo de tipos de servicio a sus respectivos catálogos
    servicios_map = {
        'transportado': datos.catalogo_transportado,
        'coffee': datos.catalogo_coffee,
        'tradicional': datos.catalogo_tradicional,
        'reposteria': datos.catalogo_reposteria,
        'concesion': datos.catalogo_concesion,
    }
    
    # Nombres para mostrar en el template
    nombres_servicios = {
        'transportado': 'Alimentación Transportada',
        'coffee': 'Coffee Break y Eventos',
        'tradicional': 'Alimentación Tradicional',
        'reposteria': 'Repostería y Snack',
        'concesion': 'Concesión de Casinos',
    }
    
    if servicio_tipo in servicios_map:
        data = {
            'catalogo_productos': servicios_map[servicio_tipo],
            'titulo_servicio': nombres_servicios[servicio_tipo],
            'servicio_tipo': servicio_tipo,
        }
        return render(request, 'templateCatalogo/catalogo2.html', data)
    else:
        # Si el servicio no existe, redirigir al catálogo principal
        return catalogoServicios(request)

def catalogoMenu(request, servicio_tipo, producto_id):
    # Mapeo de tipos de servicio a sus respectivos menús
    menus_map = {
        'transportado': datos.menu_transportado,
        'coffee': datos.menu_coffe,
        'tradicional': datos.menu_tradicional,
        'reposteria': datos.menu_reposteria,
        'concesion': datos.menu_concesion,
    }
    
    # Mapeo de nombres de productos
    productos_map = {
        'transportado': datos.catalogo_transportado,
        'coffee': datos.catalogo_coffee,
        'tradicional': datos.catalogo_tradicional,
        'reposteria': datos.catalogo_reposteria,
        'concesion': datos.catalogo_concesion,
    }
    
    if servicio_tipo in menus_map and int(producto_id) in menus_map[servicio_tipo]:
        menu_item = menus_map[servicio_tipo][int(producto_id)]
        producto_info = productos_map[servicio_tipo][int(producto_id)]
        
        data = {
            'menu_detalle': menu_item,
            'producto_nombre': producto_info['nombre'],
            'producto_imagen': producto_info['imagen'],
            'servicio_tipo': servicio_tipo,
        }
        return render(request, 'templateCatalogo/catalogo3.html', data)