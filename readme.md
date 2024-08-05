[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/L8WaA7U8)
# Catálogo de Discos de Música

## Objetivo

Desarrollar una aplicación sencilla que permita gestionar un catálogo de discos de música, implementando las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para dos entidades: Artista y Álbum.

## Descripción del Ejercicio

El estudiante debe crear una aplicación web que permita a los usuarios gestionar un catálogo de discos de música. La aplicación debe incluir las siguientes funcionalidades:


### CRUD para Artista

- **Crear:** Permitir la creación de nuevos artistas con los siguientes campos:
  - Nombre del Artista
  - País de Origen
- **Leer:** Mostrar una lista de todos los artistas registrados con opción para ver detalles.
- **Actualizar:** Permitir la edición de la información de un artista existente.
- **Eliminar:** Permitir la eliminación de un artista.

### CRUD para Álbum

- **Crear:** Permitir la creación de nuevos álbumes con los siguientes campos:
  - Título del Álbum
  - Año de Lanzamiento
  - Género
  - Artista Asociado (usando un dropdown o similar para seleccionar un artista existente)
  - Portada
- **Leer:** Mostrar una lista de todos los álbumes registrados con opción para ver detalles.
- **Actualizar:** Permitir la edición de la información de un álbum existente.
- **Eliminar:** Permitir la eliminación de un álbum.

## Requisitos Técnicos

- **Backend:** Utilizar Django para implementar la lógica del servidor y manejar las operaciones CRUD.
- **Frontend:** Crear una interfaz web simple usando HTML, CSS y las plantillas de Django.
- **Base de Datos:** Utilizar una base de datos SQLite (incluida por defecto en Django) para almacenar la información de los artistas y álbumes.
- **Protección de vistas:** Por motivos de tiempo el estudiante no implementará ninguna vista relacionada con login.


## Estructura del Proyecto

La estructura del proyecto debe ser la siguiente:

```bash
albums/              # Proyecto Django
|- __init__.py
|- asgi.py
|- settings.py
|- urls.py
|- wsgi.py
album_manager/       # Aplicación Django
|- migrations/
  |- __init__.py
|- admin.py
|- apps.py
|- models.py
|- tests.py
|- urls.py
|- views.py
.gitignore
manage.py
readme.md
requirements.txt
```

## Entregables

1. **Código Fuente:** Todo el código fuente del proyecto debe ser entregado en un repositorio de Github.

## Evaluación

1. **Funcionalidad:** El correcto funcionamiento de las operaciones CRUD para ambas entidades.
2. **Calidad del Código:** Organización, claridad y limpieza del código.
3. **Interfaz de Usuario:** Usabilidad y diseño de la interfaz web.

## Instalación del ambiente

### Requerimientos

- Python 3.10 o superior
- PostgreSQL o SQLite

### Ubuntu Linux / MacOS
Instalación de gestor de ambientes virtuales de Python
~~~
sudo apt install python3-venv
~~~
Creación del ambiente virtual
~~~
python3 -m venv .venv
~~~
Activación del ambiente virtual
~~~
source .venv/bin/activate
~~~
Instalación de dependencias de este proyecto
~~~
pip3 install -r requirements.txt
~~~
En caso de querer desactivar el ambiente usar
~~~
deactivate
~~~
### Windows
Instalación de gestor de ambientes virtuales de Python
~~~
pip install virtualenv
~~~
Creación del ambiente virtual
~~~
py -m venv .venv
~~~
Activación del ambiente virtual para CMD
~~~
.venv\Scripts\activate
~~~
Activación del ambiente virtual para PowerShell
~~~
.venv\Scripts\activate.ps1
~~~
Instalación de dependencias de este proyecto
~~~
pip install -r requirements.txt
~~~
En caso de querer desactivar el ambiente usar
~~~
deactivate
~~~

## Comandos útiles

### Iniciar servidor
#### Linux o MacOS
~~~
python3 manage.py runserver
~~~
#### Windows
~~~
python manage.py runserver
~~~

Una vez inicializado el servidor se deberá dirigir al siguiente enlace: <http://localhost:8000>

### Crear nueva aplicación
#### Linux o MacOS
~~~
python3 manage.py startapp <nombre_de_la_aplicacion>
~~~
#### Windows
~~~
python manage.py startapp <nombre_de_la_aplicacion>
~~~

### Crear Súper Usuario
#### Linux o MacOS
~~~
python3 manage.py createsuperuser
~~~
#### Windows
~~~
python manage.py createsuperuser
~~~

### Generar archivos de migración
#### Linux o MacOS
~~~
python3 manage.py makemigrations
~~~
#### Windows
~~~
python manage.py makemigrations
~~~

### Migrar a bases de datos
#### Linux o MacOS
~~~
python3 manage.py migrate
~~~
#### Windows
~~~
python manage.py migrate
~~~

### Desplegar SQL's ejecutados en migración
#### Linux o MacOS
~~~
python3 manage.py sqlmigrate pokedex 0001
~~~
#### Windows
~~~
python manage.py sqlmigrate pokedex 0001
~~~

### Almacenar depdendencias y librerías instaladas
#### Linux o MacOS
~~~
pip3 freeze > requirements.txt
~~~
#### Windows
~~~
pip freeze > requirements.txt
~~~

# Cadena de Conexión con SQLite


### SQLite
- Configurar archivo settings.py
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ```