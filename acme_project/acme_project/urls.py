from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", include("pages.urls")),
    path("admin/", admin.site.urls),
    path("birthday/", include("birthday.urls")),
]

if settings.DEBUG:  # <--- Важно для разработки
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
