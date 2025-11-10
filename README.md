# GMExpress

Sistema de gestión empresarial desarrollado con Django para el manejo de catálogos, ventas, usuarios y empresas.

## Descripción del Proyecto

GMExpress es una aplicación web diseñada para la gestión integral de operaciones comerciales. El sistema incluye módulos para:

- Gestión de catálogos de productos
- Administración de empresas
- Control de ventas
- Gestión de usuarios

## Requisitos Previos

- Python 3.8 o superior
- MySQL Server (puerto 3308)
- pip (gestor de paquetes de Python)

## Instalación

### 1. Clonar o descargar el proyecto

```bash
cd C:\Users\homer\Desktop\gmexpress
```

### 2. Crear y activar un entorno virtual (recomendado)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

Crear la base de datos en MySQL:

```sql
CREATE DATABASE gmexpress;
CREATE USER 'administrador'@'localhost' IDENTIFIED BY '12345';
GRANT ALL PRIVILEGES ON gmexpress.* TO 'administrador'@'localhost';
FLUSH PRIVILEGES;
```

Nota: Asegúrate de que MySQL esté corriendo en el puerto 3308.

### 5. Ejecutar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 7. Cargar archivos estáticos

```bash
python manage.py collectstatic --noinput
```

## Ejecución del Proyecto

### Iniciar el servidor de desarrollo

```bash
python manage.py runserver
```

El servidor estará disponible en: `http://127.0.0.1:8000/`

### Acceder al panel de administración

URL: `http://127.0.0.1:8000/admin/`

## Credenciales de Prueba

**Usuario:** admin  
**Contraseña:** 12345

## Estructura del Proyecto

```
gmexpress/
├── catalogo/          # Módulo de catálogos
├── catalogue/         # Módulo de catálogo alternativo
├── empresa/           # Gestión de empresas
├── gmexpress/         # Configuración principal del proyecto
├── media/             # Archivos multimedia subidos
├── static/            # Archivos estáticos (CSS, JS, imágenes)
├── templates/         # Plantillas HTML
├── usuarios/          # Gestión de usuarios
├── ventas/            # Módulo de ventas
├── manage.py          # Script de gestión de Django
└── requirements.txt   # Dependencias del proyecto
```

## Tecnologías Utilizadas

- Django 5.2.5
- MySQL
- Bootstrap 5 (django-crispy-forms)
- Pillow (procesamiento de imágenes)
- Python-stdnum (validación de números)

## Notas Adicionales

- El proyecto está configurado en modo DEBUG. Para producción, cambiar `DEBUG = False` en `settings.py`
- Los archivos multimedia se almacenan en la carpeta `media/`
- El idioma del sistema está configurado en español (es-cl)
- Zona horaria: America/Santiago
