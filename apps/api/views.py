"""
API views that expose endpoints from other apps.

This app acts as a router/organizer for API endpoints.
Import views from other apps and expose them here.
"""

from apps.base.views import HealthCheckAPIView

# Re-export views from other apps
__all__ = ["HealthCheckAPIView"]
