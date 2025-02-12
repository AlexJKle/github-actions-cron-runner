"""File for the config model."""

from typing import Any, Dict, List
from pydantic import BaseModel

from github_actions_cron_runner.exceptions.github_actions_cronjob_config_exceptions import (
    GithubActionCronjobConfigParseException,
)


class GithubActionCronjobConfig(BaseModel):
    """Basic config model for the cronjobs."""

    github_api_url: str
    cron: str
    display_name: str | None = None
    branch: str = "main"
    token: str | None = None

    @classmethod
    def from_config_dict(
        cls, config_dict: Dict[str, Any]
    ) -> "GithubActionCronjobConfig":
        """Converts a config dict into a GithubActionCronjobConfig object

        Args:
            config_dict: the dict that contains the info from the json.

        Raises:
            GithubActionCronjobConfigParseException: when some mandatory fields are not filled.

        Returns:
            The parsed object
        """
        # check if all mandatory fields are filled correctly
        if not config_dict.get("githubApiUrl") or not config_dict.get("cron"):
            raise GithubActionCronjobConfigParseException

        config_dict.update(
            {
                "github_api_url": config_dict["githubApiUrl"],
                "display_name": config_dict["displayName"],
            }
        )
        return GithubActionCronjobConfig(**config_dict)

    @classmethod
    def from_config_dict_list(
        cls, config_dict_list: List[Dict[str, Any]]
    ) -> List["GithubActionCronjobConfig"]:
        """Parses a list of config_dicts into a list of GithubActionCronjobConfig.

        Args:
            config_dict_list: list of config dicts to parse.

        Raises:
            GithubActionCronjobConfigParseException: when a mandatory field is not filled
                in one item.

        Returns:
            The list parsed as a list of GithubActionCronjobConfig
        """
        return [
            GithubActionCronjobConfig.from_config_dict(config_dict=config_dict)
            for config_dict in config_dict_list
        ]
