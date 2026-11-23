# Blog Django — Proyecto del curso de Python (Coderhouse)

Blog web hecho con Django. Es la evolución del blog por consola de las primeras preentregas.

Sitio online: https://oscaresluciano.pythonanywhere.com/

## Cómo ejecutar el proyecto

```bash
git clone https://github.com/oscaresluciano/blog_django.git
cd blog_django
python -m venv venv
source venv/bin/activate        # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abrir http://127.0.0.1:8000/

## Preentrega 8 — URLs, Views, Templates y Static

Flujo implementado: **Ruta → Vista → Template → Estático**.

- `blog_project/urls.py` conecta las rutas de la app con `include("posts.urls")`.
- `posts/urls.py` define las rutas `inicio` (`/`), `acerca` (`/acerca/`) y `lista_posts` (`/posts/`).
- `posts/views.py` tiene views basadas en funciones que usan `render()`.
- `posts/templates/posts/base.html` es el layout base: usa `{% load static %}`, enlaza el CSS,
  tiene el menú de navegación y el bloque `{% block content %}`.
- `inicio.html`, `acerca.html` y `lista_posts.html` heredan con `{% extends 'posts/base.html' %}`.
- `posts/static/posts/css/estilos.css` tiene los estilos del sitio, enlazado con
  `{% static 'posts/css/estilos.css' %}`.

## Preentrega 9 — Modelos, ORM y Admin

- Modelo `Post` en `posts/models.py` con los campos `titulo`, `contenido`, `autor`,
  `fecha_creacion` (`auto_now_add=True`) y `estado` (choices: borrador, publicado, archivado).
  Implementa `__str__` que devuelve el título.
- Migraciones: `python manage.py makemigrations` y `python manage.py migrate` (base SQLite `db.sqlite3`).
- Admin: `posts/admin.py` registra `Post` con `PostAdmin` (columnas título, autor, estado y fecha).
- Superusuario: `python manage.py createsuperuser`, luego entrar a `/admin/` y cargar posts.
- La view `lista_posts` consulta con el ORM
  `Post.objects.filter(estado="publicado").order_by("-fecha_creacion")`
  y el template los recorre con `{% for post in posts %}`.

## Estructura

```
blog_django/
├── manage.py
├── requirements.txt
├── blog_project/      # settings.py, urls.py
└── posts/           # models, admin, views, urls, templates/posts/, static/posts/css/
```
