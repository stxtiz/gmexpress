from django.db import models

# Create your models here.
catalogo1 = {
    'Alimentación transportada': ['transporte.jpg', 'servicio_transportado'],
    'Alimentación tradicional (presencial)': ['presencial.jpg', 'servicio_tradicional'],
    'Concesión de Casinos': ['casino.jpg', None],
    'Coffee break y eventos': ['cafeb.jpg', None],
    'Repostería y snack con tickets': ['snack.jpg', None],
}

catalogo_transportado = {
    'Almuerzo tradicional': ['almuerzo.jpg', None],
    'Vegetariano': ['vegetariano.jpg', None],
    'Vegano': ['vegano.jpg', None],
    'Hipocalórico': ['hipocalorico.jpg', None],
    'Menú especial del día' : ['especial.jpg', None],
}