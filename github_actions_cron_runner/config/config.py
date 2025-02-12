"""File for all possible configurations for the application."""

import os


GITHUB_MASTER_TOKEN_PATH = os.getenv("GITHUB_MASTER_TOKEN_PATH")
REMOVE_GITHUB_MASTER_TOKEN_AT_STARTUP = (
    False
    if os.getenv("REMOVE_GITHUB_MASTER_TOKEN_AT_STARTUP")
    and os.getenv("REMOVE_GITHUB_MASTER_TOKEN_AT_STARTUP", "true").lower()
    in ("false", "0", "no")
    else True
)

ACTION_CRON_CONFIG_PATH = os.getenv("ACTION_CRON_CONFIG_PATH")
