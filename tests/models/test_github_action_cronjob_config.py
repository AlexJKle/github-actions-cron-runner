import pytest
from github_actions_cron_runner.exceptions.github_actions_cronjob_config_exceptions import (
    GithubActionCronjobConfigParseException,
)
from github_actions_cron_runner.models.github_action_cronjob_config import (
    GithubActionCronjobConfig,
)
from tests.basic_testdata import TESTDATA_CONFIGDICT_INVALID, TESTDATA_CONFIGDICT_VALID


def test_from_config_dict() -> None:
    config = GithubActionCronjobConfig.from_config_dict(
        config_dict=TESTDATA_CONFIGDICT_VALID
    )
    assert config.github_api_url == TESTDATA_CONFIGDICT_VALID["githubApiUrl"]
    assert config.cron == TESTDATA_CONFIGDICT_VALID["cron"]
    assert config.branch == TESTDATA_CONFIGDICT_VALID["branch"]
    assert config.display_name == TESTDATA_CONFIGDICT_VALID["displayName"]
    assert config.token == TESTDATA_CONFIGDICT_VALID["token"]


def test_from_config_dict_for_invalid_config() -> None:
    with pytest.raises(GithubActionCronjobConfigParseException):
        GithubActionCronjobConfig.from_config_dict(
            config_dict=TESTDATA_CONFIGDICT_INVALID
        )


def test_parse_config_list() -> None:
    config_list = GithubActionCronjobConfig.from_config_dict_list(
        config_dict_list=[TESTDATA_CONFIGDICT_VALID]
    )
    assert len(config_list) == 1
    assert config_list[0].github_api_url == TESTDATA_CONFIGDICT_VALID["githubApiUrl"]
    assert config_list[0].cron == TESTDATA_CONFIGDICT_VALID["cron"]
    assert config_list[0].branch == TESTDATA_CONFIGDICT_VALID["branch"]
    assert config_list[0].display_name == TESTDATA_CONFIGDICT_VALID["displayName"]
    assert config_list[0].token == TESTDATA_CONFIGDICT_VALID["token"]


def test_parse_config_list_with_one_invalid() -> None:
    with pytest.raises(GithubActionCronjobConfigParseException):
        GithubActionCronjobConfig.from_config_dict_list(
            config_dict_list=[TESTDATA_CONFIGDICT_INVALID]
        )


def test_parse_config_list_with_mixed_valid_and_invalid() -> None:
    with pytest.raises(GithubActionCronjobConfigParseException):
        GithubActionCronjobConfig.from_config_dict_list(
            config_dict_list=[TESTDATA_CONFIGDICT_VALID, TESTDATA_CONFIGDICT_INVALID]
        )
