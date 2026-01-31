"""
API URL Configuration

This file organizes all API endpoints.
Import views from other apps and expose them here.
"""

from django.urls import path

from apps.base.views import HealthCheckAPIView

app_name = "api"

urlpatterns = [
    # Example: Health check endpoint from base app
    path("health/", HealthCheckAPIView.as_view(), name="health"),
]
