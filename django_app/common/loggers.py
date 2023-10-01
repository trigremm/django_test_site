# django_app/common/loggers.py

import sys

from loguru import logger

# Export the loggers for use in other modules
__all__ = ["logger"]

# Default logger configuration
logger.remove()
logger.add(sys.stderr, level="INFO", enqueue=True)
# logger.add(
#     "/app/logs/app.log",
#     rotation="10 MB",
#     format="{time} {module}.{function}:{line} {level} {message}",
#     level="WARNING",
#     enqueue=True,
#     compression="zip",
# )
