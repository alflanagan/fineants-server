"""
Command to import data from a Bank of America statement in CSV form.
"""
import csv

from datetime import date, datetime
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Reads a Bank of America statement CSV file and saves the transactions."

    def add_arguments(self, parser):
        parser.add_argument(
            "file",
            type=lambda f: open(f, newline=""),
            help="A Bank of America statement download in CSV format",
        )

    def handle(self, *args, **options):
        for line in csv.reader(options['file']):
            if line[0] != 'Posted Date':
                trans_date = datetime.strptime(line[0], '%m/%d/%Y').date()
                print(trans_date)
