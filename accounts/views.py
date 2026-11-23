from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import PerfilForm, RegistroForm, UsuarioForm
from .models import Perfil


def registro(request):
    if request.user.is_authenticated:
        return redirect("perfil")

    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            # El perfil se crea por señal; get_or_create lo asegura igual
            Perfil.objects.get_or_create(user=usuario)
            login(request, usuario)
            messages.success(request, f"¡Bienvenido, {usuario.username}! Tu cuenta fue creada.")
            return redirect("perfil")
    else:
        form = RegistroForm()

    return render(request, "accounts/registro.html", {"form": form})


@login_required
def perfil(request):
    perfil_usuario, _ = Perfil.objects.get_or_create(user=request.user)
    return render(request, "accounts/perfil.html", {"perfil": perfil_usuario})


@login_required
def editar_perfil(request):
    perfil_usuario, _ = Perfil.objects.get_or_create(user=request.user)

    if request.method == "POST":
        usuario_form = UsuarioForm(request.POST, instance=request.user)
        # request.FILES trae el avatar subido
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil_usuario)
        if usuario_form.is_valid() and perfil_form.is_valid():
            usuario_form.save()
            perfil_form.save()
            messages.success(request, "Perfil actualizado.")
            return redirect("perfil")
    else:
        usuario_form = UsuarioForm(instance=request.user)
        perfil_form = PerfilForm(instance=perfil_usuario)

    context = {"usuario_form": usuario_form, "perfil_form": perfil_form}
    return render(request, "accounts/editar_perfil.html", context)
