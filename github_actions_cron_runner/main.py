import logging
import os
import time
import schedule

from github_actions_cron_runner.config.config import ACTION_CRON_CONFIG_PATH
from github_actions_cron_runner.utils.cron_config_utils import load_cron_config
from github_actions_cron_runner.utils.cron_utils import cron_check_and_run

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Main function that loads config and runs the scheduler."""
    if not ACTION_CRON_CONFIG_PATH:
        logger.error("ACTION_CRON_CONFIG_PATH environment variable is not set!")
        return

    if not os.path.exists(ACTION_CRON_CONFIG_PATH):
        logger.error(f"Config file {ACTION_CRON_CONFIG_PATH} not found!")
        return

    logger.info(f"Loading config from {ACTION_CRON_CONFIG_PATH}")
    config_list = load_cron_config(ACTION_CRON_CONFIG_PATH)

    logger.info(f"Found {len(config_list)} jobs in the config.")
    for index, config in enumerate(config_list, start=1):
        job_name = config.display_name or f"Job {index}"
        logger.info(
            f"Job {index}: {job_name}\n"
            f"  GitHub Endpoint: {config.github_api_url}\n"
            f"  Cron Schedule: {config.cron}"
        )

    schedule.every().minute.do(lambda: cron_check_and_run(config_list=config_list))

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
