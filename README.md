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

## Preentrega 10 — CRUD de posts con imágenes

### Operaciones disponibles

| Operación | URL | View |
|---|---|---|
| Listar | `/posts/` | `lista_posts` |
| Ver detalle | `/posts/<id>/` | `detalle_post` |
| Crear | `/post/nuevo/` | `crear_post` |
| Editar | `/posts/<id>/editar/` | `editar_post` |
| Eliminar (con confirmación) | `/posts/<id>/eliminar/` | `eliminar_post` |

- `posts/forms.py`: `PostForm` hereda de `forms.ModelForm` con los campos
  `titulo`, `contenido`, `autor`, `estado` e `imagen`.
- Templates: `lista_posts.html`, `detalle_post.html`, `post_form.html` y `post_confirm_delete.html`,
  todos heredan de `posts/base.html`.

### Manejo de imágenes

- Nueva dependencia: **Pillow** (`pip install Pillow`, incluida en `requirements.txt`).
- Campo en el modelo: `imagen = models.ImageField(upload_to='posts/', null=True, blank=True)`.
- `settings.py`: `MEDIA_URL = '/media/'` y `MEDIA_ROOT = BASE_DIR / 'media'`.
- `blog_project/urls.py` sirve los archivos media en desarrollo con
  `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`.
- Las views de crear y editar pasan `request.FILES` al formulario.
- `post_form.html` usa `enctype="multipart/form-data"`.
- Si un post no tiene imagen, el template muestra un mensaje en lugar de romperse.

### Cómo probar la carga de imágenes

1. Ir a `/post/nuevo/`, completar el formulario y elegir una imagen.
2. Guardar: se abre el detalle del post con la imagen.
3. La imagen queda guardada en `media/posts/`.
4. Desde "Editar" se puede cambiar o quitar la imagen.

## Estructura

```
blog_django/
├── manage.py
├── requirements.txt
├── blog_project/      # settings.py, urls.py
├── media/posts/     # imágenes subidas (no se sube al repo)
└── posts/           # models, forms, admin, views, urls, templates/posts/, static/posts/css/
```
