from django.shortcuts import render

# Datos de ejemplo (en el Módulo 9 se reemplazan por la base de datos)
POSTS_DE_EJEMPLO = [
    {
        "titulo": "Mi primer post en Django",
        "autor": "Luciano",
        "contenido": "El blog dejó la consola y ahora es un sitio web con rutas, vistas y templates.",
    },
    {
        "titulo": "Herencia de templates",
        "autor": "Luciano",
        "contenido": "Con base.html escribo el menú una sola vez y todas las páginas lo reutilizan.",
    },
]


def inicio(request):
    return render(request, "posts/inicio.html")


def acerca(request):
    return render(request, "posts/acerca.html")


def lista_posts(request):
    context = {"posts": POSTS_DE_EJEMPLO}
    return render(request, "posts/lista_posts.html", context)
