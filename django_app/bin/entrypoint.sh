#!/usr/bin/env bash
set -Eeuxo pipefail

# Variables
export DJANGO_SETTINGS_MODULE=core.settings

# https://stackoverflow.com/a/23378780
LOGICAL_CORES=$(lscpu -p | grep -E -v '^#' | wc -l)
PHYSICAL_CORES=$(lscpu -p | grep -E -v '^#' | sort -u -t, -k 2,4 | wc -l)
LOG_TO_PHY_RATIO=$((LOGICAL_CORES / PHYSICAL_CORES))

# Prepare the environment and run migrations
# python manage.py collectstatic
python manage.py migrate

# collect static
python manage.py collectstatic --noinput

# Run the server
gunicorn core.asgi:application --worker-class uvicorn.workers.UvicornWorker -w $((2*$PHYSICAL_CORES+1)) --bind 0.0.0.0:8000 &

# Run the Celery worker - for production run in separate container
celery -A core worker --loglevel=info --concurrency=2 -Q high_priority,default,low_priority &
# celery -A core worker --loglevel=info --concurrency=2  &

# Run the Celery beat - for production run in separate container
celery -A core beat --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?
