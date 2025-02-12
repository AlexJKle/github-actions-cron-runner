import logging
from typing import List
from croniter import croniter
from datetime import datetime

from github_actions_cron_runner.models.github_action_cronjob_config import (
    GithubActionCronjobConfig,
)
from github_actions_cron_runner.utils.github_utils import trigger_github_action
from github_actions_cron_runner.utils.master_token_utils import load_master_token

logger = logging.getLogger(__name__)

MASTER_TOKEN = load_master_token()


def cron_check_and_run(config_list: List[GithubActionCronjobConfig]) -> None:
    """Checks if the current time matches the cron expression and runs the job if it does."""
    now = datetime.now().replace(second=0, microsecond=0)

    for index, config in enumerate(config_list, start=1):
        token = config.token or MASTER_TOKEN or ""
        job_name = config.display_name or f"Job {index}"

        iter = croniter(config.cron, now)
        _ = iter.get_prev(datetime).replace(second=0, microsecond=0)
        _ = iter.get_current(datetime).replace(second=0, microsecond=0)
        next_run = iter.get_next(datetime).replace(second=0, microsecond=0)

        logger.info(
            f"Checking cron '{config.cron}' for job {job_name}. "
            f"Next scheduled run: {next_run.strftime('%Y-%m-%d %H:%M')}"
        )

        if now == next_run:
            logger.info(
                f"Executing job {job_name} for {config.github_api_url} on branch {config.branch}"
            )
            response = trigger_github_action(
                config.github_api_url, token, config.branch
            )
            if 200 <= response.status_code < 300:
                logger.info(
                    f"Successfully executed job {job_name}. Status code: {response.status_code}"
                )
            else:
                logger.error(
                    f"Failed to execute job {job_name}. Status code: {response.status_code}"
                )
        else:
            logger.info(f"No job to run this minute for {job_name}.")
