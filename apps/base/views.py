from django.conf import settings
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.base.serializers import HealthCheckSerializer, ProtectedDataSerializer
from core.constants import BRAND_NAME, VERSION


class IndexView(TemplateView):
    """Landing page."""

    template_name = "base/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand_name"] = BRAND_NAME
        context["docs_disabled"] = settings.ENVIRONMENT == settings.PROD
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


class ProtectedAPIView(APIView):
    """
    Protected API endpoint that requires JWT authentication.

    This endpoint demonstrates how to protect an API route with JWT tokens.
    Users must include a valid JWT token in the Authorization header to access this endpoint.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Protected endpoint that returns user information."""
        serializer = ProtectedDataSerializer(
            {
                "message": f"Welcome {request.user.username}! This is a protected endpoint.",
                "user_id": request.user.id,
                "username": request.user.username,
                "is_authenticated": request.user.is_authenticated,
            }
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
