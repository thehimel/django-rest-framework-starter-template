#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import argparse
import os
import sys

from core.constants.env import Environment


def _apply_env_arg():
    """
    Parse --env / -e from sys.argv and set os.environ["ENVIRONMENT"] before Django loads.

    Input is case-insensitive (e.g. dev, DEV); the value is always set in capital (DEV, PROD).
    This allows running management commands against a specific environment without
    changing the .env file (e.g. python manage.py migrate --env=prod).
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--env",
        "-e",
        choices=[e.value for e in Environment],
        type=lambda s: s.upper(),
        metavar="ENV",
        help="Override environment (case-insensitive; stored as %(choices)s) without changing .env",
    )
    args, remaining = parser.parse_known_args(sys.argv[1:])
    if args.env is not None:
        os.environ["ENVIRONMENT"] = args.env  # Always uppercase
    sys.argv[:] = [sys.argv[0]] + remaining


def main():
    """Run administrative tasks."""
    _apply_env_arg()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
