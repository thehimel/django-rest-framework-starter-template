"""Application environment enum (used by constants loader and manage.py --env)."""

from enum import Enum


class Environment(str, Enum):
    """Application environment."""

    DEV = "DEV"
    PROD = "PROD"
