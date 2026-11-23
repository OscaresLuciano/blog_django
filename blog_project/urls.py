from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cuentas/", include("accounts.urls")),
    path("", include("posts.urls")),
]

# Sirve los archivos estáticos (CSS) mientras DEBUG = True
urlpatterns += staticfiles_urlpatterns()

# Sirve los archivos media (imágenes de posts y avatares) en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
