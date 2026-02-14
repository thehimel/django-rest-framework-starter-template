"""Environment-specific constants."""

from decouple import config

from core.constants.env import Environment


def _load_constants():
    """Load dev or prod constants module based on ENVIRONMENT."""
    selected_environment = Environment(config("ENVIRONMENT", default=Environment.DEV.value))
    if selected_environment == Environment.DEV:
        from core.constants import dev as constants_module
    elif selected_environment == Environment.DEV_REMOTE:
        from core.constants import dev as constants_module

        constants_module.DATABASE_URL = config("DATABASE_URL")
    else:
        from core.constants import prod as constants_module
    return selected_environment, constants_module


SELECTED_ENVIRONMENT, constants = _load_constants()
