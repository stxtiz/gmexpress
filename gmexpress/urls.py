from django.contrib import admin
from django.urls import path



from empresa import views as vista
from catalogo import views as catalogo_vista
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vista.inicio, name='inicio'),
    
    #path catalogos    
    path('Catalogo/', catalogo_vista.catalogoServicios, name='catalogo'),
    path('Transportado/', catalogo_vista.catalogoTransporte, name='servicio_transportado'),
    path('Tradicional/', catalogo_vista.catalogoServicios, name='servicio_tradicional'),
    path('Coffe/', catalogo_vista.catalogoCoffe, name='servicio_coffe'),
    path('Reposteria/', catalogo_vista.catalogoReposteria, name='servicio_reposteria'),
    #path nosotros
    path('nosotros/', vista.info_empresa, name='info_empresa'),
]
