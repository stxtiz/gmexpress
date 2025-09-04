from django.contrib import admin
from django.urls import path

from empresa import views as vista
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vista.inicio, name='inicio'),
    path('nosotros', vista.info_empresa, name='info_empresa'),
]
