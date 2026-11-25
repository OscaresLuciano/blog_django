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

## Preentrega 11 — Autenticación, usuarios y perfiles

Se creó la app `accounts` (registrada en `INSTALLED_APPS`).

- **Registro** (`/cuentas/registro/`): formulario `RegistroForm` basado en `UserCreationForm`
  (usuario, email, nombre, apellido y contraseña). Al registrarse se crea el `Perfil`
  y el usuario queda logueado.
- **Login** (`/cuentas/login/`): `LoginView` nativa de Django con template propio.
- **Logout** (botón "Cerrar sesión" del menú): `LogoutView` (por POST), redirige al listado de posts.
- **Redirecciones** en `settings.py`: `LOGIN_URL = 'login'`,
  `LOGIN_REDIRECT_URL = 'lista_posts'`, `LOGOUT_REDIRECT_URL = 'lista_posts'`.
- **Cambio de contraseña**: `/cuentas/password/`.

### Modelo Perfil

`accounts/models.py`: `Perfil` tiene `user` (`OneToOneField` con `User`), `biografia` (`TextField`),
`link_web` (`URLField` opcional) y `avatar` (`ImageField(upload_to="avatares/")`).

El perfil se crea automáticamente al crear un usuario mediante una señal `post_save`
(`accounts/signals.py`) y, además, la view de registro lo asegura con
`Perfil.objects.get_or_create(user=usuario)`. Está registrado en el admin.

### Avatares

Se guardan en `media/avatares/` usando la configuración `MEDIA_URL` / `MEDIA_ROOT`.
La view `editar_perfil` pasa `request.FILES` al formulario y el template usa
`enctype="multipart/form-data"`. Si no hay avatar, se muestra un texto alternativo.

- Ver perfil: `/cuentas/perfil/` · Editar biografía y avatar: `/cuentas/perfil/editar/`

### Rutas protegidas (requieren login con `@login_required`)

- Crear post: `/post/nuevo/`
- Editar post: `/posts/<id>/editar/`
- Eliminar post: `/posts/<id>/eliminar/`
- Perfil y edición de perfil: `/cuentas/perfil/`, `/cuentas/perfil/editar/`
- Cambio de contraseña: `/cuentas/password/`

Si un visitante anónimo entra a esas URLs, es redirigido al login.
El listado y el detalle de posts siguen siendo públicos.

El menú cambia según el usuario: los anónimos ven "Iniciar sesión" y "Registrarse";
los logueados ven "Hola, usuario", "Crear post", "Mi perfil" y "Cerrar sesión".

### Migraciones

Después de clonar o actualizar el proyecto:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Estructura

```
blog_django/
├── manage.py
├── requirements.txt
├── blog_project/      # settings.py, urls.py
├── media/           # posts/ y avatares/ (no se sube al repo)
├── posts/           # models, forms, admin, views, urls, templates/posts/, static/posts/css/
└── accounts/        # Perfil, forms, signals, views, urls, templates/accounts/
```

## Entregas

- Preentrega 8: https://github.com/OscaresLuciano/blog_django/tree/preentrega-8
- Preentrega 9: https://github.com/OscaresLuciano/blog_django/tree/preentrega-9
- Preentrega 10: https://github.com/OscaresLuciano/blog_django/tree/preentrega-10
- Preentrega 11: https://github.com/OscaresLuciano/blog_django/tree/preentrega-11
