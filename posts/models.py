from django.db import models


class Post(models.Model):
    BORRADOR = "borrador"
    PUBLICADO = "publicado"
    ARCHIVADO = "archivado"
    ESTADOS = [
        (BORRADOR, "Borrador"),
        (PUBLICADO, "Publicado"),
        (ARCHIVADO, "Archivado"),
    ]

    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default=BORRADOR)

    class Meta:
        ordering = ["-fecha_creacion"]
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.titulo
