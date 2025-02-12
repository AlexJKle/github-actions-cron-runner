# GitHub Actions Cron Runner

This is a lightweight Python-based scheduler that triggers GitHub Actions workflows at specified cron intervals. It runs inside a Docker container and provides optional support for a master authentication token.

## Features
- Schedule and trigger GitHub Action workflows using cron expressions.
- Supports individual authentication tokens per workflow.
- Allows the use of a master GitHub token, which is removed from the filesystem after startup for security.
- Runs inside a Docker container.

## Configuration
The application requires a JSON configuration file that specifies the GitHub workflows and their schedules.

### JSON Config Structure
```json
[
  {
    "githubApiUrl": "https://api.github.com/repos/user/repo/actions/workflows/workflow.yml/dispatches",
    "cron": "*/5 * * * *",
    "branch": "main",
    "token": "your_personal_access_token",
    "displayName": "My Workflow"
  }
]
```

### Fields:
- `githubApiUrl`: The GitHub API URL for the workflow dispatch endpoint.
- `cron`: A cron expression defining the schedule.
- `branch`: (Optional) The branch to trigger the workflow on (default: `main`).
- `token`: (Optional) A personal access token for authentication. If not provided, the master token is used.
- `displayName`: (Optional) A name for logging purposes.

## Environment Variables
| Variable                                | Description                                                | Default | Required |
|-----------------------------------------|------------------------------------------------------------|---------|----------|
| `ACTION_CRON_CONFIG_PATH`               | Path to the JSON config file                               |         | Yes      |
| `GITHUB_MASTER_TOKEN_PATH`              | Path to a file containing a master GitHub token            |         | No       |
| `REMOVE_GITHUB_MASTER_TOKEN_AT_STARTUP` | Whether the master token file should be deleted on startup |    true | No       |

### Master Token Handling
If `GITHUB_MASTER_TOKEN_PATH` is set, the program will:
1. Read the token from the file.
2. Remove the file after reading (except if deletion is turned off with `REMOVE_GITHUB_MASTER_TOKEN_AT_STARTUP` set to false).
3. Use this token for all requests unless a job-specific token is provided in the JSON config.

## Running with Docker
### Build the Image
```sh
docker build -t alexjkle/github-actions-cron-runner:{tag} .
```

### Run the Container
```sh
docker run --rm -e ACTION_CRON_CONFIG_PATH=/app/config/config.json -v /path/to/config:/app/config alexjkle/github-actions-cron-runner
```

If using a master token file:
```sh
docker run --rm -e ACTION_CRON_CONFIG_PATH=/app/config.json -e GITHUB_MASTER_TOKEN_PATH=/app/github_master_token -v /path/to/config.json:/app/config.json -v /path/to/token:/app/github_master_token github-cron-runner
```

## License
MIT License.

