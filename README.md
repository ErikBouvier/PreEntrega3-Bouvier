
 PETSERVICE

 Descripción
PetService es una aplicación web desarrollada con Python y Django que permite gestionar información sobre mascotas, propietarios y veterinarios. La aplicación incluye formularios para registrar y buscar mascotas, listado de servicios y resultados de búsqueda.

 Estructura del Proyecto

- static: Archivos estáticos como CSS.
- templates: Plantillas HTML para las vistas de la aplicación.
- __pycache__: Archivos compilados de Python.
- db.sqlite3: Base de datos SQLite del proyecto.
- manage.py: Script de administración de Django.
- petservice: Directorio principal de la aplicación Django.
  - __init__.py: Archivo de inicialización del módulo.
  - admin.py: Configuración del panel de administración de Django.
  - apps.py: Configuración de la aplicación.
  - forms.py: Formularios de Django.
  - models.py: Definición de los modelos de datos.
  - urls.py: Definición de las rutas de la aplicación.
  - views.py: Vistas de la aplicación.

 Uso
- Accede a la aplicación en tu navegador en `http://127.0.0.1:8000/`.
- Utiliza los formularios para registrar y buscar información sobre mascotas, propietarios y veterinarios.

 Funcionalidades
- Registro de Mascotas: Permite registrar nuevas mascotas con información detallada.
- Búsqueda de Mascotas: Funcionalidad para buscar mascotas registradas en la base de datos.
- Gestión de Propietarios: Registro y gestión de información de propietarios de mascotas.
- Gestión de Veterinarios: Registro y gestión de información de veterinarios.
- Páginas de Agradecimiento: Páginas que se muestran después de completar formularios.
