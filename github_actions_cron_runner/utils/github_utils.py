import requests


def trigger_github_action(url: str, token: str, branch: str) -> requests.Response:
    """
    Triggers a GitHub action workflow.

    Args:
        url (str): The GitHub API URL to trigger the workflow.
        token (str): The GitHub token for authentication.
        branch (str): The branch on which to trigger the workflow.

    Returns:
        requests.Response: The HTTP response object.
    """
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
    }
    payload = {"ref": branch}
    response = requests.post(url, headers=headers, json=payload)

    return response
