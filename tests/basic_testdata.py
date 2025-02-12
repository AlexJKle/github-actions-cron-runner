TESTDATA_CONFIGDICT_VALID = {
    "githubApiUrl": "https://api.github.com/repos/user/repo/actions/workflows/workflow.yml/dispatches",  # noqa: E501
    "cron": "*/5 * * * *",
    "branch": "main",
    "token": "your_personal_access_token",
    "displayName": "My Workflow",
}

TESTDATA_CONFIGDICT_INVALID = {
    "githubApiUrli": "https://api.github.com/repos/user/repo/actions/workflows/workflow.yml/dispatches",  # noqa: E501
    "cron": "*/5 * * * *",
    "token": "your_personal_access_token",
    "displayName": "My Workflow",
}
