#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import logging
import time

from django.db.utils import OperationalError

logger = logging.getLogger(__name__)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fineants.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    db_errors = 0

    try:
        execute_from_command_line(sys.argv)
    except OperationalError as oe:
        logger.warning(oe)
        db_errors += 1
        if db_errors > 2:
            raise
        time.sleep(10)


if __name__ == '__main__':
    main()
