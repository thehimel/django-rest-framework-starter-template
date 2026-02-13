from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from core.constants import constants

schema_view = get_schema_view(
    openapi.Info(
        title=constants.BRAND_NAME,
        default_version="v1",
        description="OpenAPI Specification",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
