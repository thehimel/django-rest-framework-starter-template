from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.base.serializers import HealthCheckSerializer
from core.constants import BRAND_NAME, VERSION


class IndexView(TemplateView):
    """Landing page."""

    template_name = "base/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand_name"] = BRAND_NAME
        return context


class HealthCheckAPIView(APIView):
    """
    Simple API endpoint example.
    This demonstrates how to create and expose an API endpoint.
    """

    permission_classes = []  # Public endpoint for demonstration

    def get(self, request):
        """Health check endpoint."""
        serializer = HealthCheckSerializer(
            {"status": "healthy", "message": f"{BRAND_NAME} API is running", "version": VERSION}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
