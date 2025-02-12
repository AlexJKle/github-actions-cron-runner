import json
from unittest.mock import patch, mock_open

from github_actions_cron_runner.utils.cron_config_utils import load_cron_config
from github_actions_cron_runner.models.github_action_cronjob_config import (
    GithubActionCronjobConfig,
)


def test_load_cron_config() -> None:
    mock_data = '[{"displayName": "Job 1", "githubApiUrl": "https://api.github.com", "cron": "* * * * *"}]'
    expected_config = [
        GithubActionCronjobConfig(
            display_name="Job 1",
            github_api_url="https://api.github.com",
            cron="* * * * *",
        )
    ]

    with patch("builtins.open", mock_open(read_data=mock_data)) as mock_file:
        with patch("json.load", return_value=json.loads(mock_data)) as mock_json_load:
            config = load_cron_config("dummy_path")
            assert (
                config == expected_config
            ), f"Expected {expected_config}, but got {config}"
            mock_file.assert_called_once_with("dummy_path", "r", encoding="utf-8")
            mock_json_load.assert_called_once()
