from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Perfil


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    first_name = forms.CharField(max_length=150, required=False, label="Nombre")
    last_name = forms.CharField(max_length=150, required=False, label="Apellido")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        labels = {"first_name": "Nombre", "last_name": "Apellido", "email": "Email"}


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ["biografia", "link_web", "avatar"]
        labels = {
            "biografia": "Biografía",
            "link_web": "Sitio web (opcional)",
            "avatar": "Avatar",
        }
        widgets = {
            "biografia": forms.Textarea(attrs={"rows": 5}),
        }
