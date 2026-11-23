from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post


def inicio(request):
    return render(request, "posts/inicio.html")


def acerca(request):
    return render(request, "posts/acerca.html")


# ---------- READ ----------
def lista_posts(request):
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    context = {
        "posts": posts
    }
    return render(request, "posts/lista_posts.html", context)


def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "posts/detalle_post.html", {"post": post})


# ---------- CREATE ----------
def crear_post(request):
    if request.method == "POST":
        # request.FILES trae la imagen subida
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, "Post creado correctamente.")
            return redirect("detalle_post", pk=post.pk)
    else:
        form = PostForm(initial={"estado": Post.PUBLICADO})

    context = {"form": form, "titulo_pagina": "Nuevo post"}
    return render(request, "posts/post_form.html", context)


# ---------- UPDATE ----------
def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post actualizado correctamente.")
            return redirect("detalle_post", pk=post.pk)
    else:
        form = PostForm(instance=post)

    context = {"form": form, "post": post, "titulo_pagina": f"Editar: {post.titulo}"}
    return render(request, "posts/post_form.html", context)


# ---------- DELETE ----------
def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        if post.imagen:
            post.imagen.delete(save=False)
        post.delete()
        messages.success(request, "Post eliminado.")
        return redirect("lista_posts")

    return render(request, "posts/post_confirm_delete.html", {"post": post})
