from rest_framework import serializers


class HealthCheckSerializer(serializers.Serializer):
    """Simple serializer for health check endpoint."""

    status = serializers.CharField(read_only=True)
    message = serializers.CharField(read_only=True)
    version = serializers.CharField(read_only=True)
