from django.contrib import admin
from django.urls import path,include

from empresa import views as vista
from catalogo import views as catalogo_vista
from usuarios import views as vistas
from catalogue import views
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', vista.inicio, name='inicio'),
    
    #path catalogos
    path('catalogo/', catalogo_vista.catalogoServicios, name='catalogo'),
    path('catalogo/<str:servicio_tipo>/', catalogo_vista.catalogoProductos, name='catalogo_productos'),
    
    #path menu detalles
    path('catalogo/<str:servicio_tipo>/<int:producto_id>/', catalogo_vista.catalogoMenu, name='menu_detalle'),
    
    #path nosotros
    path('nosotros/', vista.info_empresa, name='info_empresa'),
    #path servicios
    path('servicioAdd/', views.crear_servicio, name='crearServicio'),
    path('servicios/', views.mostrar_servicios, name='mostrarServicios'),
    path('servicioCargar/<int:id>',views.cargar_servicio, name='cargarServicio'),
    path('modificarServicio/<int:id>',views.modificar_servicio, name='modificarServicio'),
    path('servicioEliminar/<int:id>',views.eliminar_servicio, name='eliminarServicio'),


    #path categorias
    path('categoriaAdd/', views.crear_categoria, name='crearCategoria'),
    path('categorias/', views.mostrar_categorias, name='mostrarCategorias'),
    path('categoriaCargar/<int:id>',views.cargar_categoria, name='cargarCategoria'),
    path('categoriaEdit/<int:id>',views.modificar_categoria, name='modificarCategoria'),
    path('categoriaEliminar/<int:id>',views.eliminar_categoria, name='eliminarCategoria'),
    
    
    
    #path usuarios
    path('accounts/',include('django.contrib.auth.urls')),
    path('usuarioAdd/',vistas.crear_usuario, name='crearUsuarios'),
    path('usuarioEdit/<int:usuario_id>/', vistas.cargar_editar_usuario, name='editarUsuario'),
    path('usuarioEditado/<int:usuario_id>/', vistas.editar_usuario, name='usuarioEditado'),
    path('usuarioDelete/<int:usuario_id>/', vistas.eliminar_usuario, name='eliminarUsuario'),
    path('usuarios/', vistas.listar_usuarios, name='listarUsuarios'),
    


    #path productos
    path('mostrar_productos/', views.mostrar_productos, name='mostrar_productos'),

    path('editar_producto/', views.editar_producto, name='editar_producto'),

    path('eliminar_producto/', views.eliminar_producto, name='eliminar_producto'),
    
    path('productos/', views.productos, name='productos'),

    path('crear_producto/', views.crear_producto, name='crear_producto'),
]
