"""Production environment constants."""

from decouple import config

BRAND_NAME = config("BRAND_NAME", default="Core")
VERSION = config("VERSION", default="1.0.0")

FRONTEND_URL = config("FRONTEND_URL", default="")
DJANGO_BACKEND_HOST = config("DJANGO_BACKEND_HOST")

ALLOWED_HOSTS = [DJANGO_BACKEND_HOST, ".vercel.app"]
CORS_ALLOWED_ORIGINS = [FRONTEND_URL]
CSRF_TRUSTED_ORIGINS = [FRONTEND_URL]

DEBUG = config("DEBUG", cast=bool, default=False)

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

DATABASE_URL = config("DATABASE_URL")
