"""Utils for the master token."""

import os
from github_actions_cron_runner.config.config import (
    GITHUB_MASTER_TOKEN_PATH,
    REMOVE_GITHUB_MASTER_TOKEN_AT_STARTUP,
)

_master_token: str | None = None


def load_master_token() -> str | None:
    """
    Load the master token from the specified file path.

    This function checks if the master token is already loaded. If not, it reads the token
    from the file specified by GITHUB_MASTER_TOKEN_PATH, stores it in the _master_token variable,
    and optionally removes the file if REMOVE_GITHUB_MASTER_TOKEN_AT_STARTUP is set to True.

    Returns:
        str | None: The loaded master token, or None if the token could not be loaded.
    """
    global _master_token

    if _master_token is not None:
        return _master_token

    if GITHUB_MASTER_TOKEN_PATH and os.path.exists(GITHUB_MASTER_TOKEN_PATH):
        with open(GITHUB_MASTER_TOKEN_PATH, "r", encoding="utf-8") as token_file:
            _master_token = token_file.read().strip()

        if REMOVE_GITHUB_MASTER_TOKEN_AT_STARTUP:
            os.remove(GITHUB_MASTER_TOKEN_PATH)

    return _master_token
