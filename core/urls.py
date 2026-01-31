from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from core.views import schema_view

urlpatterns = [
    path("", include("apps.base.urls")),
    path("api/", include("apps.api.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    # To serve static files in debug mode
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # To serve media files in debug mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # To serve OpenAPI Specification
    urlpatterns += [
        path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
        path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    ]
