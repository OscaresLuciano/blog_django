from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"
    verbose_name = "Cuentas de usuario"

    def ready(self):
        # Conecta la señal que crea el Perfil al registrar un usuario
        from . import signals  # noqa: F401
