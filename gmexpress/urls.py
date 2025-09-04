from django.contrib import admin
from django.urls import path



from empresa import views as vista
from catalogo import views as catalogo_vista
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vista.inicio, name='inicio'),
    
        
    path('catalogo/', catalogo_vista.catalogo, name='catalogo'),
    path('nosotros/', vista.info_empresa, name='info_empresa'),
]