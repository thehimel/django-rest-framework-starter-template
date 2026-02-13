"""Development environment constants."""

from decouple import config

BRAND_NAME = config("BRAND_NAME", default="Core")
VERSION = config("VERSION", default="1.0.0")

FRONTEND_URL = config("FRONTEND_URL", default="http://localhost:3000")
DJANGO_BACKEND_HOST = config("DJANGO_BACKEND_HOST", default="localhost")

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
CORS_ALLOWED_ORIGINS = ["http://localhost:3000", "http://127.0.0.1:3000"]
CSRF_TRUSTED_ORIGINS = ["http://localhost:3000", "http://127.0.0.1:3000"]

DEBUG = True

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# None means use default SQLite path in settings (BASE_DIR-dependent).
DATABASE_URL = None
