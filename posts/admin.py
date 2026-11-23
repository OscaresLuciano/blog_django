from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "estado", "fecha_creacion")
    list_filter = ("estado", "fecha_creacion")
    search_fields = ("titulo", "contenido", "autor")


admin.site.register(Post, PostAdmin)
