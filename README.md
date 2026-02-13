# Django REST Framework Starter Template

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-6.0+-green.svg)
![DRF](https://img.shields.io/badge/DRF-3.16+-red.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Maintained](https://img.shields.io/badge/Maintained-yes-green.svg)
![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)
![isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)

A production-ready Django REST Framework starter template with JWT authentication, CORS configuration, API documentation, and environment-based settings.

## Features

- **Django REST Framework** with JWT authentication
- **CORS** configured for frontend communication
- **API Documentation** with Swagger/ReDoc (drf-yasg)
- **Environment-based configuration** (Development/Production)
- **Database** support (SQLite for dev, PostgreSQL/MySQL via DATABASE_URL for production)
- **Security headers** and best practices
- **Structured app organization** with `apps/` directory
- **Code quality tools**: Black, isort, and pre-commit hooks
- **Testing**: Django test framework with coverage reporting

## Quick Start

### Initial Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <repository>
   ```

2. **Run initialization script**
   ```bash
   chmod +x init.sh
   ./init.sh
   ```

   This will:
   - Upgrade pip and install dependencies
   - Install pre-commit hooks
   - Run database migrations

3. **Format existing code** (first time setup)
   ```bash
   pre-commit run --all-files
   ```

4. **Start the development server**
   ```bash
   python manage.py runserver
   ```

5. **Access the application**
   - Landing page: http://localhost:8000/
   - API docs: http://localhost:8000/swagger/ (in DEBUG mode)
   - Admin: http://localhost:8000/admin/

## Project Structure

```
├── apps/
│   ├── api/               # API app - organizes and exposes API endpoints
│   │   ├── urls.py        # API URL routing
│   │   └── views.py      # Re-exports views from other apps
│   └── base/              # Base app - contains business logic
│       ├── serializers.py # DRF serializers
│       ├── views.py       # API views and templates
│       └── templates/     # HTML templates
├── core/                  # Django project settings
│   ├── settings.py        # Main configuration
│   ├── urls.py            # Root URL configuration
│   ├── views.py           # Schema view for API docs
│   └── constants/         # Environment-specific constants (dev/prod)
│       ├── __init__.py    # Loader; exports SELECTED_ENVIRONMENT, constants
│       ├── env.py         # Environment enum (DEV/PROD)
│       ├── dev.py         # Development constants
│       └── prod.py        # Production constants
├── manage.py
├── requirements.txt
├── .env.template
├── pyproject.toml         # Black and isort configuration
├── .pre-commit-config.yaml # Pre-commit hooks configuration
├── .coveragerc            # Coverage configuration
├── coverage.sh            # Run test coverage
├── init.sh                 # Initialization script
└── erd.sh                  # Generate Entity Relationship Diagram
```

## Configuration

The project uses environment variables for configuration. Copy `.env.template` to `.env` and update the values:

- `SECRET_KEY`: Django secret key
- `ENVIRONMENT`: `DEV` or `PROD` — controls which constants are loaded from `core/constants/dev.py` or `core/constants/prod.py`
- `DATABASE_URL`: Database connection string (for production)
- `FRONTEND_URL`: Frontend URL for CORS

Environment-based values (e.g. `ALLOWED_HOSTS`, `DEBUG`, `CORS_*`) are defined per environment in `core/constants/dev.py` and `core/constants/prod.py`; the loader in `core/constants/__init__.py` selects the correct set based on the `ENVIRONMENT` env var and exposes it as `SELECTED_ENVIRONMENT`. Tests always use an in-memory SQLite database and never connect to the production database.

### Overriding environment for management commands

By default, **ENVIRONMENT** is read from `.env` (or the default). You can override it for a single run by passing `--env` (or `-e`) to any management command. Values are those in [core/constants/env.py](core/constants/env.py) (`Environment` enum): `DEV`, `PROD`. Input is **case-insensitive** (e.g. `prod`, `PROD`); the value is always set in capital.

```bash
python manage.py migrate --env=prod
python manage.py runserver --env prod
python manage.py test -e prod
```

The flag is parsed in [manage.py](manage.py) before Django loads, so the chosen environment is used for settings and constants. When you omit `--env`, `.env` (or the default) is used as before.

## Code Formatting

This project uses [Black](https://github.com/psf/black) and [isort](https://github.com/PyCQA/isort) for code formatting, enforced via pre-commit hooks.

### Format all files
```bash
pre-commit run --all-files
```

### Format specific files
```bash
black <file_or_directory>
isort <file_or_directory>
```

Pre-commit hooks run automatically on every commit. To bypass (not recommended):
```bash
git commit --no-verify
```

## Testing

The project includes test coverage configuration and automated test execution via pre-commit hooks.

### Run tests
```bash
python manage.py test .
```

### Run coverage
```bash
./coverage.sh
```

This generates an HTML coverage report in `htmlcov/` directory. Coverage configuration is defined in [`.coveragerc`](.coveragerc).

### Pre-commit Testing

Tests run automatically before each commit via pre-commit hooks (see [`.pre-commit-config.yaml`](.pre-commit-config.yaml)). The hook runs Django tests to ensure code quality before commits.

## Authentication

JWT authentication is configured and ready to use. See [docs/authentication.md](docs/authentication.md) for detailed instructions on:
- Obtaining JWT tokens
- Refreshing tokens
- Using tokens in API requests
- Token configuration

**Quick Start:**
1. Create a superuser: `python manage.py createsuperuser`
2. Obtain tokens: `POST /api/token/` with username and password
3. Use token: Include `Authorization: Bearer <token>` header in API requests
   - In Swagger UI: Click "Authorize" and enter `Bearer <token>` (include the "Bearer " prefix)

## API Documentation

When running in DEBUG mode, access API documentation at:
- Swagger UI: `/swagger/`
- ReDoc: `/redoc/`

## Entity Relationship Diagram (ERD)

Generate a visual diagram of your database models:

```bash
./erd.sh
```

This creates `docs/design/images/models.jpg` showing all models and their relationships.

**Note**: Requires Graphviz to be installed on your system:
- macOS: `brew install graphviz`
- Ubuntu/Debian: `sudo apt-get install graphviz`
- Windows: Download from [Graphviz website](https://graphviz.org/download/)
