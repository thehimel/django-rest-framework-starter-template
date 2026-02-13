# Steps - How This Repository Was Built

This document outlines the step-by-step process of building this Django REST Framework starter template.

## 1. Initial Django Project Setup

Created the base Django project:

```bash
django-admin startproject core .
```

## 2. Created Base App

Created the base app and moved it to `apps/` directory:

```bash
python manage.py startapp base
mkdir -p apps
mv base apps/base
```

Updated `apps/base/apps.py` to use `apps.base` naming convention.

## 3. Created API App

Created the API app to organize and expose API endpoints:

```bash
python manage.py startapp api
mv api apps/api
```

Updated `apps/api/apps.py` to use `apps.api` naming convention.

## 4. Configured REST Framework

Added Django REST Framework dependencies and configuration:

- Added `rest_framework`, `rest_framework_simplejwt` to `INSTALLED_APPS`
- Configured JWT authentication in `REST_FRAMEWORK` settings
- Set up `SIMPLE_JWT` configuration with 30-day token lifetime

## 5. Added CORS Support

Configured CORS for frontend communication:

- Added `corsheaders` to `INSTALLED_APPS`
- Added `CorsMiddleware` at the top of middleware stack
- Configured CORS settings based on environment (DEV/PROD)
- Set `CORS_ALLOW_CREDENTIALS = True` for JWT authentication

## 6. Added API Documentation

Set up Swagger/ReDoc documentation:

- Added `drf_yasg` to `INSTALLED_APPS`
- Created `core/views.py` with `schema_view` configuration
- Added Swagger and ReDoc URLs (available in DEBUG mode)

## 7. Environment-Based Configuration

Set up environment-based settings:

- Created `core/constants/` package with:
  - `__init__.py`: `Environment` enum (DEV/PROD) and loader that imports `dev` or `prod` based on the `ENVIRONMENT` env var and exports `SELECTED_ENVIRONMENT` and `constants`
  - `dev.py`: development constants (BRAND_NAME, VERSION, ALLOWED_HOSTS, CORS, DEBUG, security flags, DATABASE_URL=None for SQLite)
  - `prod.py`: production constants (same names, values from env/config)
- Updated `settings.py` to use `SELECTED_ENVIRONMENT` and `constants` from `core.constants`; all environment-dependent settings read from `constants.*`
- Tests use in-memory SQLite (`"test" in sys.argv`) so the test runner never touches the production database
- Created `.env.template` with all required variables

## 8. Database Configuration

Configured database settings:

- Added `dj-database-url` for flexible database configuration
- Set up SQLite for development (default), PostgreSQL/MySQL via `constants.DATABASE_URL` for production
- Tests use in-memory SQLite so the test runner never touches the production database (avoids hangs in CI/prod-like environments)
- Added connection pooling with `conn_max_age=600`

## 9. Security Headers

Added production-ready security settings:

- HSTS configuration
- SSL redirect (production only)
- Secure cookies (production only)
- XSS protection
- CSRF trusted origins

## 10. Static and Media Files

Configured static and media file handling:

- Set `STATIC_ROOT` and `STATIC_URL`
- Configured `STATICFILES_DIRS`
- Set `MEDIA_ROOT` and `MEDIA_URL`
- Added static/media serving in DEBUG mode

## 11. Created Landing Page

Added a simple landing page in the base app:

- Created `apps/base/templates/base/index.html` with monochromatic design
- Created `IndexView` (TemplateView) in `apps/base/views.py`
- Added root URL route in `apps/base/urls.py`

## 12. Created Example API Endpoint

Added a health check API endpoint as an example:

- Created `HealthCheckSerializer` in `apps/base/serializers.py`
- Created `HealthCheckAPIView` (APIView) in `apps/base/views.py`
- Exposed via `apps/api/urls.py` at `/api/health/`
- Demonstrates the pattern for creating and exposing APIs

## 12.1. Added JWT Token Endpoints

Added JWT token endpoints to enable authentication:

- Added `TokenObtainPairView` and `TokenRefreshView` imports to `apps/api/urls.py`
- Added `/api/token/` endpoint for obtaining access and refresh tokens
- Added `/api/token/refresh/` endpoint for refreshing access tokens
- Created `docs/authentication.md` with comprehensive authentication documentation

These endpoints allow users to authenticate and obtain JWT tokens for API access. See [docs/authentication.md](../authentication.md) for detailed usage instructions.

## 13. Code Formatting Setup

Configured code quality tools:

- Added `black>=24.4.2` and `isort>=5.13.2` to requirements
- Created `pyproject.toml` with black and isort configuration (120 char line length)
- Set up pre-commit hooks with `.pre-commit-config.yaml`
- Added `pre-commit>=3.6.0` to requirements

## 14. Pre-commit Hooks

Set up automated code formatting:

- Created `.pre-commit-config.yaml` with:
  - Basic file checks (trailing whitespace, file endings, etc.)
  - Black code formatter
  - isort import sorter
  - Django test execution
- Added `pre-commit install` to `init.sh`

## 15. ERD Generation Setup

Added Entity Relationship Diagram generation:

- Added `django-extensions>=3.2.3` and `pydotplus>=2.0.2` to requirements
- Added `django_extensions` to `INSTALLED_APPS`
- Created `erd.sh` script to generate model diagrams
- Created `docs/design/` directory structure
- Added ERD documentation

## 16. Initialization Script

Created `init.sh` for quick project setup:

- Upgrades pip
- Installs dependencies
- Installs pre-commit hooks
- Runs database migrations

## 17. Documentation

Created comprehensive documentation:

- Main `README.md` with quick start guide
- `docs/steps/README.md` (this file) documenting the build process
- `docs/design/README.md` for ERD generation
- Updated project structure in all docs

## 18. Vercel Deployment Notes

- **Build pipeline:** Vercel’s configuration lives in [`vercel.json`](../../vercel.json), which points the Python server to `core/wsgi.py` and runs `build.sh` via the static builder.
- **Pyproject issue:** Vercel’s `uv lock` step errors with `No 'project' table found` when `pyproject.toml` lacks a `[project]` table; see [`docs/issues.md`](../issues.md) for the logged error.

## Project Structure

```
jobrio-backend/
├── apps/
│   ├── __init__.py
│   ├── api/               # API app - organizes and exposes API endpoints
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── urls.py        # API URL routing
│   │   └── views.py       # Re-exports views from other apps
│   └── base/              # Base app - contains business logic
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── serializers.py  # DRF serializers
│       ├── views.py        # API views and template views
│       ├── urls.py         # Base app URLs
│       ├── templates/      # HTML templates
│       │   └── base/
│       │       └── index.html
│       └── migrations/
├── core/                   # Django project settings
│   ├── __init__.py
│   ├── settings.py        # Main configuration
│   ├── urls.py            # Root URL configuration
│   ├── views.py           # Schema view for API docs
│   ├── constants/         # Environment-specific constants (dev/prod)
│   │   ├── __init__.py    # Environment enum and loader
│   │   ├── dev.py         # Development constants
│   │   └── prod.py        # Production constants
│   ├── wsgi.py
│   └── asgi.py
├── docs/
│   ├── design/
│   │   ├── images/        # ERD diagrams
│   │   └── README.md
│   └── steps/
│       └── README.md      # This file
├── manage.py
├── requirements.txt
├── .env.template
├── pyproject.toml         # Black and isort configuration
├── .pre-commit-config.yaml # Pre-commit hooks configuration
├── .coveragerc            # Coverage configuration
├── coverage.sh            # Run test coverage
├── init.sh                 # Initialization script
├── erd.sh                  # Generate Entity Relationship Diagram
└── README.md
```

## Key Features Implemented

### REST Framework
- JWT Authentication configured
- CORS enabled for frontend communication
- API documentation with drf-yasg (Swagger/ReDoc)

### Database
- Environment-based configuration (SQLite dev, PostgreSQL/MySQL prod)
- Connection pooling

### Security
- Environment-based security settings
- CORS configured for frontend origin
- HSTS and security headers enabled in production

### Code Quality
- Black code formatter (120 character line length)
- isort import sorter (black-compatible)
- Pre-commit hooks to enforce formatting automatically
- Django test framework with coverage reporting
- Automated test execution via pre-commit hooks

### Development Tools
- django-extensions for ERD generation
- Entity Relationship Diagram generator (`./erd.sh`)
- Initialization script for quick setup
