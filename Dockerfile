FROM python:3.13-slim

# Install Poetry
RUN pip install --no-cache-dir poetry

WORKDIR /app
COPY . /app

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Set required environment variable (must be supplied at runtime)
ENV ACTION_CRON_CONFIG_PATH=""

# Run the main Python script when the container starts
CMD ["poetry", "run", "python", "-m", "github_actions_cron_runner.main"]