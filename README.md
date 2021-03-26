MyBlog: Breve introducción a Django
=====================

## 1. El proyecto

Este proyecto es una breve introducción a los componentes básicos de Django creando un pequeño blog personal.

### Pre-requisitos

Es indispensable tener conocimientos mínimos de:

* Python
* HTML

Es muy recomendable:

* Programación orientada a objetos

## 2. Qué es Django

Django es un framework web escrito en Python que se define como:

> El framework para perfeccionistas con fechas de entrega.

## 3. Instalar Django

Primero instalamos Django utilizando el gestor de paquetes de Python: `pip`

```bash
pip install django
```

Ahora iniciamos un proyecto de Django con la herramienta `django-admin`:

```bash
django-admin startproject myblog
```

Si todo ha ido bien deberíamos tener un directorio nuevo con los ficheros iniciales de Django:

```
myblog/
├── manage.py
└── myblog
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

* `manage.py` es una utilidad para gestionar el proyecto Django
* `myblog/__init__.py` denota que un directorio es un paquete Python
* `myblog/settings.py` es donde reside la configuración de Django
* `myblog/urls.py` es donde definiremos las rutas (URLs) de nuestra web
* `myblog/asgi.py` y `myblog/wsgi.py` son puntos de entrada para servidores webs

Por ahora solamente vamos a modificar `settings.py` para cambiar el idioma a español, para ello buscamos la siguiente línea:

```python
LANGUAGE_CODE = 'en-us'
```

Y la cambiamos por:

```python
LANGUAGE_CODE = 'es'
```

## 4. Las aplicaciones

El código en Django se divide en _aplicaciones_. Cada aplicación reside en un directorio distinto, vamos a crear nuestra primera aplicación:

```bash
python manage.py startapp blog
```

Deberíamos tener un nuevo directorio, llamado `blog`, con el siguiente contenido:

```
blog/
├── migrations
│   └── __init__.py
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

Por ahora vamos a olvidarnos del directorio `migrations` y del archivo `tests.py`.

Vamos a ver para qué utilizaremos cada fichero:

* `apps.py`: aquí definiremos la configuración de la aplicación
* `models.py`: aquí crearemos los modelos de nuestra aplicación
* `admin.py`: aquí definiremos los modelos que aparecerán en el panel de administración
* `views.py`: aquí definiremos las vistas (páginas) de nuestra aplicación

Vamos a utilizar además un fichero, que creararemos más adelante, llamado `urls.py`, donde configuraremos las rutas de nuestra aplicación.

Si queremos utilizar una aplicación en nuestro proyecto Django, debemos agregarla a la lista de aplicaciones en `settings.py`, así que buscamos la lista `INSTALLED_APPS` en dicho archivo y agregamos la siguiente línea al final:

```python
INSTALLED_APPS = [
    # ...

    'blog.apps.BlogConfig',
]
```

> Se utiliza la ruta a la configuración de la aplicación siguiendo el formato de `imports` de Python: `directorio.fichero.NombreClase`

## 5. Los modelos

En Django los modelos son clases que heredan de `Model`, cuyas propiedades son los propios campos del modelo; los modelos se crean en el fichero `models.py` de cada aplicación. En el caso de nuestro blog, vamos a definir un modelo `Entrada` con los campos `titulo` y `texto` (por ahora).

```python
from django.db import models

class Entrada(models.Model):
    titulo = models.CharField('título', max_length=140)
    texto = models.TextField('texto', max_length=1000)
```

Para poder utilizar un modelo en Django tenemos que crear una _migración_, esto es, un fichero que describe los cambios que hemos realizado en el modelo; Django utilizará estas _migraciones_ para estructurar la base de datos.

> Por defecto Django crea una base de datos SQLite en un archivo (`db.sqlite3`) dentro de nuestro proyecto, de forma que no tendremos que gestionar bases de datos para comenzar a desarrollar.

Para crear migraciones disponemos del siguiente comando:

```bash
python manage.py makemigrations
```

Que debería generar una salida como esta:

```
Migrations for 'blog':
  blog/migrations/0001_initial.py
    - Create model Entrada
```

Una vez creada la migración, la aplicamos con el siguiente comando:

```bash
python manage.py migrate
```

Como es la primera vez que lo hacemos, se aplicarán también las migraciones de los modelos de Django: usuarios, permisos, ...

## 6. El panel de administración

Ahora que tenemos nuestro modelo creado, vamos a incluirlo en el panel de administración para poder realizar operaciones sobre él. Para ello modificamos el fichero `admin.py` agregando una clase que identifique nuestro modelo:

```python
from django.contrib import admin
from .models import Entrada

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'texto')
```

En la clase que hemos creado definimos las propiedades del modelo que se mostrarán en las listas del panel de administración (propiedad `list_display`), y registramos la clase junto al modelo con el decorador `@admin.register`.

Para poder acceder al panel de administración debemos crear primero un súper-usuario, para ello utilizamos el siguiente comando:

```bash
python manage.py createsuperuser
```

Nos solicitará los datos del usuario por terminal, los introducimos y se creará el usuario:

```
Nombre de usuario (leave blank to use 'usuario'): admin
Dirección de correo electrónico: admin@myblog.com
Password:
Password (again):
Superuser created successfully.
```

Sólo nos queda iniciar el servidor web de Django para poder iniciar sesión y acceder al panel:

```bash
python manage.py runserver
```

Deberíamos obtener una salida similar a la siguiente:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 29, 2020 - 16:07:36
Django version 3.0.3, using settings 'myblog.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Tal y como podemos ver, nuestro sitio web es accesible en la URL `http://127.0.0.1:8000/`.

En el fichero `myblog/urls.py` está definida la ruta al panel de administración, que por defecto es `'/admin'`, es decir, que podremos acceder a él en la URL `http://127.0.0.1:8000/admin/`.

En el panel de administración podemos crear, modificar y eliminar usuarios, grupos y, por supuesto, nuestros modelos.

## 7. Las vistas

Ya hemos terminado la parte oculta de nuestro blog, ahora vamos a crear el sitio web público utilizando vistas.

### Una vista básica

#### La plantilla

Creamos un directorio llamado `templates` dentro de nuestra aplicación blog, dentro creamos un archivo `index.html` (nombre arbitrario), e incluimos el siguiente contenido:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Mi Blog</title>
</head>
<body>
    <p>Hola Mundo!</p>
</body>
</html>
```

#### La función de vista

Ahora vamos a definir la vista que mostrará este archivo. En el fichero `views.py` de nuestra aplicación agregamos el siguiente código:

```python
def vista_indice(request):
    return render(request, 'index.html')
```

Esta es la forma más básica de una vista: una función que recibe una petición HTTP y devuelve la respuesta HTTP (en este caso, compilando la plantilla `index.html`).

#### Las rutas

Nos falta asignar esta vista a una ruta, para ello creamos un fichero `urls.py` en nuestra aplicación con el siguiente contenido:

```python
from django.urls import path
from .views import vista_indice

urlpatterns = [
    path('', vista_indice),
]
```

Importamos la vista y la agregamos como ruta (`path`) a una lista de rutas (`urlpatterns`).

Finalmente incluímos estas rutas en el fichero `urls.py` del directorio de proyecto (`myblog/urls.py`); agregamos la lista de rutas de nuestra aplicación blog a la lista de rutas del proyecto bajo la ruta (`blog/`):

```python
urlpatterns = [
    path('blog/', include('blog.urls')),

    # ...
]
```

Si no hemos apagado el servidor web, éste se debería reiniciar automáticamente para reflejar los cambios, con lo cual solamente nos queda acceder a la URL `http://127.0.0.1:8000/blog/` para ver nuestro _Hola Mundo_.

### Una vista con clase

En Django existe una forma más avanzada de crear vistas utilizando clases. Vamos a modificar la vista que ya hemos creado para utilizar este método.

#### La clase

Reemplazamos el contenido del fichero `views.py` con el siguiente contenido:

```python
from django.views.generic import TemplateView

class VistaIndice(TemplateView):
    template_name = 'index.html'
```

La vista es simplemente una clase que hereda de `View`, o de una subclase de `View`, en este caso utilizamos `TemplateView`, que nos muestra una plantilla si le indicamos su nombre (`template_name`).

#### La ruta

También debemos actualizar la creación de la ruta en el fichero `urls.py` de nuestta aplicación blog:

```python
from django.urls import path
from .views import VistaIndice

urlpatterns = [
    path('', VistaIndice.as_view()),
]
```

La llamada a `.as_view()` en una subclase de `View` genera una función que utiliza dicha clase para crear la vista.

Si volvemos a acceder a la URL `http://127.0.0.1:8000/blog/`, podremos ver que nada ha cambiado; lo cual nos indica que:

1. No hemos roto nada.
2. El nuevo código tiene una funcionalidad equivalente al anterior.

### El sistema de plantillas

Django trae un sistema de plantillas bastante completo, vamos a aprender a utilizarlo.

Vamos a extraer la parte común de nuestro HTML a un fichero que vamos a llamar `base.html` (nombre arbitrario). La zona donde vayamos a incluir nuestro contenido será una etiqueta `block` del sistema de plantillas de Django:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Mi Blog</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

Para extender esta plantilla utilizaremos la etiqueta `extends` y llenaremos el `block` con el contenido real.

Modificamos `index.html` para utilizar esta funcionalidad:

```html
{% extends 'base.html' %}

{% block content %}
    <p>Hola Mundo!</p>
{% endblock content %}
```

Si volvemos a recargar nuestro navegador, deberíamos ver (de nuevo) el mismo contenido.

### Vistas que hacen cosas

Ahora que sabemos crear vistas y utilizar plantillas, vamos a crear una vista para mostrar las entradas de nuestro blog. Para ello creamos una nueva clase de vista que herede de `ListView` (en lugar de `TemplateView`). `ListView` es una **vista genérica**, simplemente indicamos el modelo y la plantilla, y Django se encargará del resto. El contenido de `views.py` queda como sigue:

```python
from django.views.generic import ListView, TemplateView
from .models import Entrada

# ...

class VistaLista(ListView):
    model = Entrada
    template_name = 'entradas.html'
```

Creamos la plantilla `entradas.html` con el siguiente contenido:

```html
{% extends 'base.html' %}

{% block content %}
    {% for entrada in object_list %}
        <h1>{{ entrada.titulo }}</h1>
        <p>{{ entrada.texto }}</p>
    {% endfor %}
{% endblock content %}
```

Utilizamos un bucle `for` para mostrar las propiedades de nuestro modelo. Por defecto Django proporciona la lista de una `ListView` en la variable `object_list`.

Solamente nos falta agregar la vista a las rutas en el `urls.py` de nuestra aplicación blog:

```python
from .views import VistaIndice, VistaLista

urlpatterns = [
    # ...
    path('entradas/', VistaLista.as_view()),
]
```

Si navegamos a la URL `http://127.0.0.1:8000/blog/entradas`, podremos ver las entradas que hayamos creado en el panel de administración.

#### Rutas de vistas genéricas en Django

Disponemos de la opción de no especificar el nombre de la plantilla en `ListView`: por defecto Django utilizará aquella que se llame `APP/MODELO_list.html` (siendo `APP` el nombre de la aplicación y `MODELO` el nombre del modelo, ambos en minúscula). Para este caso sería: `blog/entrada_list.html`.

Creamos el directorio `blog` dentro del directorio `templates` de nuestra aplicación y renombramos el fichero `entradas.html` a `entrada_list.html`.

Finalmente eliminamos la siguiente línea de nuestra clase `VistaLista`:

```python
    template_name = 'entradas.html'
```

### Rutas con parámetros

Ahora vamos a crear una vista detalle para nuestras entradas. Utilizamos la vista genérica `DetailView` indicando el modelo; la ruta de la plantilla es como en `ListView` pero cambiando `list` por `detail`. Agregamos la siguiente clase a nuestro `views.py`:

```python
from django.views.generic import DetailView, ListView, TemplateView

# ...

class VistaDetalle(DetailView):
    model = Entrada
```

En la plantilla (`blog/entrada_detail.html`) disponemos de la entrada en la variable `object`, y el contenido de la plantilla sería tan simple como:

```html
{% extends 'base.html' %}

{% block content %}
    <h1>{{ object.titulo }}</h1>
    <p>{{ object.texto }}</p>
{% endblock content %}
```

Para indicar a Django qué entrada queremos ver, vamos a crear una ruta con un parámetro, dicho parámetro va a ser el identificador de la entrada. Para ello incluimos el parámetro en la ruta de la siguiente forma (`urls.py`):

```python
from .views import VistaIndice, VistaLista, VistaDetalle

urlpatterns = [
    # ...
    path('entrada/<pk>/', VistaDetalle.as_view()),
]
```

Et voilá, ya tenemos nuestra vista detalle.

### Enlaces dinámicos

Para poder navegar el sitio web correctamente necesitamos crear enlaces, para ello vamos a dar nombre a cada vista en el fichero `urls.py` de nuestra aplicación:

```python
# ...

urlpatterns = [
    path('', VistaIndice.as_view(), name='indice'),
    path('entradas/', VistaLista.as_view(), name='lista'),
    path('entrada/<pk>/', VistaDetalle.as_view(), name='detalle'),
]
```

A continuación modificamos la plantilla `index.html` para agregar un enlace a la lista de entradas:

```html
{% extends 'base.html' %}

{% block content %}
    <p>Hola Mundo!</p>

    <p><a href="{% url 'lista' %}">Ir a la lista</a></p>
{% endblock content %}
```

La etiqueta `{% url 'NOMBRE_VISTA' %}` nos genera un enlace a la vista indicada. Opcionalmente podemos indicarle los parámetros que tenga la ruta, por ejemplo, para agregar enlaces a las vistas detalle en nuestra lista de entradas (`entrada_list.html`):

```html
{% extends 'base.html' %}

{% block content %}
    {% for entrada in object_list %}
        <h1><a href="{% url 'detalle' entrada.id %}">{{ entrada.titulo }}</a></h1>
        <p>{{ entrada.texto }}</p>
    {% endfor %}
{% endblock content %}
```

También vamos a agregar un enlace de vuelta a la lista en la vista detalle:

```html
{% extends 'base.html' %}

{% block content %}
    <p><a href="{% url 'lista' %}">Volver a la lista</a></p>

    <h1>{{ object.titulo }}</h1>
    <p>{{ object.texto }}</p>
{% endblock content %}
```

## 8. Utilizando el sistema de usuarios de Django

A continuación, vamos a agregar un campo _autor_ al modelo Entrada, de forma que podamos mostrar quién ha escrito cada entrada del blog; pero vamos a permitir que las entradas puedan ser anónimas, es decir, que no tengan asociado ningún usuario. Para ello, agregamos un campo de clave foránea al modelo, e indicamos que debe ser hacia el modelo de usuario que nos crea Django, y que debe permitir nulos (`null=True`) y que el formulario del panel de administración nos deje crear una entrada con ese campo en blanco (`blank=True`):

```python
from django.contrib.auth import get_user_model

class Entrada(models.Model):
    ...

    user = models.ForeignKey(
        get_user_model(), models.CASCADE,
        null=True, blank=True
    )

    ...
```

Ahora solamente tendríamos que crear y ejecutar una migración para este nuevo campo:

```bash
python manage.py makemigrations
python manage.py migrate
```

Si queremos mostrar el campo en nuestros templates, solamente tenemos que imprimir el usuario como cualquier otro atributo del objeto:

```html
<h3>By: {{ object.autor.username }}</h3>
```

Pero esto quedaría muy feo cuando no hubiese un autor definido, entonces vamos a encapsularlo en un bloque condicional:

```html
{% if object.autor %}
    <h3>By: {{ object.autor.username }}</h3>
{% endif %}
```

Así, cuando no exista un valor para el campo `autor`, no se mostrará la etiqueta `h3`.

## 9. Siguientes pasos

En la documentación de Django hay un tutorial mucho más extenso y con más detalle: [https://docs.djangoproject.com/en/3.0/intro/tutorial01/](Tutorial Django 3.0).
