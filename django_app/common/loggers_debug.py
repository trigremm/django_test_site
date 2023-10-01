# django_app/common/loggers_debug.py
# this module is django independent


import sys

from loguru import logger

__all__ = ["logger"]

# Configure the debug logger
logger.remove()
logger.add(sys.stderr, level="DEBUG", enqueue=True)
