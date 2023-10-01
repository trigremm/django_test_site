# Base image
FROM python:3.11.3-slim-bullseye

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_HOME="/opt/poetry" \
    PATH="$POETRY_HOME/bin:$PATH"

# Build arguments
ARG POETRY_VERSION=1.4.2

# Install system dependencies
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        git \
        build-essential 

# Cleanup cache to reduce image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY ./poetry.lock ./pyproject.toml /app/

# Upgrade pip and setuptools, Install poetry and project dependencies
RUN --mount=type=cache,target=/root/.cache \
    pip install --upgrade pip setuptools && \
    pip install poetry==${POETRY_VERSION} && \
    poetry config virtualenvs.create false && \
    poetry install --only main --compile --no-root --no-interaction

# Cleanup unnecessary packages to reduce image size
RUN apt-get purge -y \
    git \
    build-essential

# Copy the rest of the application code
COPY . /app

# Expose port
EXPOSE 8000

# Runtime command
CMD ["./bin/entrypoint.sh"]
