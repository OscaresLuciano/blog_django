# Blog Django

Proyecto base de un blog web desarrollado con Django.

## Descripción

Este repositorio contiene la estructura inicial de un proyecto Django para construir un blog.
Incluye la configuración base del proyecto (`blog_project`) y una aplicación llamada `posts`.

Configuración aplicada:

- App `posts` registrada en `INSTALLED_APPS` como `posts.apps.PostsConfig`.
- Idioma: español de Argentina (`es-ar`).
- Zona horaria: `America/Argentina/Buenos_Aires`.

## Requisitos

- Python 3.10 o superior
- Git

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/oscaresluciano/blog_django.git
```

Entrar a la carpeta del proyecto:

```bash
cd blog_django
```

Crear el entorno virtual:

```bash
python -m venv venv
```

Activar el entorno virtual:

En Windows PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

En Linux o macOS:

```bash
source venv/bin/activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Aplicar las migraciones iniciales:

```bash
python manage.py migrate
```

## Ejecutar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador:

http://127.0.0.1:8000/

Para detener el servidor: `Ctrl + C`.

## Estructura

```
blog_django/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── blog_project/      -> configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── posts/             -> app principal del blog
```

## Aplicaciones

- **posts**: aplicación inicial para manejar las publicaciones del blog.

