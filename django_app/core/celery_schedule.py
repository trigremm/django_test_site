# django_app/core/celery_schedule.py
CELERY_BEAT_SCHEDULE = {
    "task-hello-i-am-periodic-task": {
        "task": "polls.tasks.hello_i_am_periodic_task",
        "schedule": 60 * 5,  # runs every 5 minutes
        "options": {
            "queue": "high_priority"  # or "default" or "low_priority" depending on which queue you want to use
        },
    },
}
