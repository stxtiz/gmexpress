from django.db import models

# Create your models here.
catalogo1 = {
    'Alimentación transportada': ['transporte.jpg', 'servicio_transportado'],
    'Alimentación tradicional (presencial)': ['presencial.jpg', 'servicio_tradicional'],
    'Concesión de Casinos': ['casino.jpg', 'servicio_concesion'],
    'Coffee break y eventos': ['cafeb.jpg', 'servicio_coffe'],
    'Repostería y snack con tickets': ['snack.jpg', 'servicio_reposteria'],
}

catalogo_transportado = {
    'Almuerzo tradicional': ['almuerzo.jpg', None],
    'Vegetariano': ['vegetariano.jpg', None],
    'Vegano': ['vegano.jpg', None],
    'Hipocalórico': ['hipocalorico.jpg', None],
    'Menú especial del día' : ['especial.jpg', None],
}

catalogo_coffee = {
    'Sándwiches': ['sandwiches.jpg', None],
    'Jugos naturales': ['jugos.jpg', None],
    'Repostería': ['reposteria.jpg', None],
    'Colaciones dulces': ['colacion.jpg', None],
    'Colaciones saladas': ['colacion2.jpg', None],
}

catalogo_tradicional = {
    'Menú Ejecutivo': ['ejecutivo.jpg', None],
    'Menú Saludable': ['saludable.jpg', None],
    'Desayuno Completo': ['desayuno.jpg', None],
    'Cena Ligera': ['cena.jpg', None],
    'Menú Regional': ['regional.jpg', None],
}

catalogo_reposteria = {
    'Queques': ['queques.jpg', None],
    'Tortas': ['tortas.jpg', None],
    'Galletas': ['galletas.jpg', None],
    'Brownies': ['brownies.jpg', None],
    'Muffins': ['muffins.jpg', None],
}

catalogo_concesion = {
    'personal de aseo ': ['aseo.jpg', None],
    'personal de alimentación': ['alimentacion.jpg', None],
    'personal de montaje': ['montaje.jpg', None],
    'personal administrativo': ['administrativo.jpg', None],
    'personal de mantención': ['mantencion.jpg', None]

}
