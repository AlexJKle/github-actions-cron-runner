"""Utils for the cron config."""

import json
from typing import List

from github_actions_cron_runner.models.github_action_cronjob_config import (
    GithubActionCronjobConfig,
)


def load_cron_config(file_path: str) -> List[GithubActionCronjobConfig]:
    """Loads the JSON configuration file."""
    with open(file_path, "r", encoding="utf-8") as file:
        file_contents = json.load(file)

    return GithubActionCronjobConfig.from_config_dict_list(
        config_dict_list=file_contents
    )
