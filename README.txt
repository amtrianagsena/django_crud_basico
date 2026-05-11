proyecto Django:

manage.py: punto de entrada para comandos de Django.
settings.py: configuración del proyecto (base de datos, aplicaciones, etc).
urls.py: enrutamiento del sitio.
models.py: definición de modelos (tablas).
templates/, static/: para HTML y recursos.

Revisar conexión a la bd en el archivo settings.py

1. Instalar Python> En el bash: python --version
--
2. Instalar Django> pip install django
3. Ubicarse en la carpeta raiz donde esta manage.py
4. Migrar la base de datos>
python manage.py makemigrations
Si es el caso: pip install pymysql
python manage.py migrate (tener XAMPP activo y la bd)
5. Crear superusuario panel de admin django> python manage.py createsuperuser
*Seguir indicaciones usuario y contraseña.
6. Ejecutar el servidor> python manage.py runserver
*Cuando salga el mensaje:Starting development server at http://127.0.0.1:8000/
7. Ir al navegador y en la url agregar> http://127.0.0.1:8000/
8. Detener la ejecución en el bach Ctrl + C
9. Acceder al panel de administración en la url> http://127.0.0.1:8000/admin/

Basado en el tutorial: https://www.youtube.com/watch?v=ezIj71CX944

--
***Usar entorno virtual
python -m venv env
env\Scripts\activate
--usar cmd si se tiene permisos NO powershell
pip install django
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass (si se tiene problemas de permisos de instalación)
pip install pymysql
pip install Pillow (para las imágenes que maneja la bd)

***Usar SQLite por permisos de actualización mariadb
project/settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
Luego sigue:
python manage.py makemigrations
python manage.py migrate
etc...
