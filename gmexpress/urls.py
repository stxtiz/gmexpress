from django.contrib import admin
from django.urls import path

from empresa import views as vista
from catalogo import views as catalogo_vista
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vista.inicio, name='inicio'),
    
    #path catalogos    
    path('Catalogo/', catalogo_vista.catalogoServicios, name='catalogo'),
    path('Transportado/', catalogo_vista.catalogoProductos, {'servicio_tipo': 'transportado'}, name='servicio_transportado'),
    path('Tradicional/', catalogo_vista.catalogoProductos, {'servicio_tipo': 'tradicional'}, name='servicio_tradicional'),
    path('Coffe/', catalogo_vista.catalogoProductos, {'servicio_tipo': 'coffee'}, name='servicio_coffe'),
    path('Reposteria/', catalogo_vista.catalogoProductos, {'servicio_tipo': 'reposteria'}, name='servicio_reposteria'),
    path('Concesion/', catalogo_vista.catalogoProductos, {'servicio_tipo': 'concesion'}, name='servicio_concesion'),
    
    #path nosotros
    path('nosotros/', vista.info_empresa, name='info_empresa'),
]
