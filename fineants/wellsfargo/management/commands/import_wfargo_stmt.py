"""
Command to import data from a Wells Fargo statement PDF.
"""
import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from djmoney.money import Money

from wellsfargo.models import WellsFargoStmtTrans


class Command(BaseCommand):
    help = "Reads a Wells Fargo Statement PDF and saves the transactions."

    def add_arguments(self, parser):
        parser.add_argument(
            "file",
            type=lambda f: open(f, newline=""),
            help="A Wells Fargo statement download in PDF format",
        )

    def handle(self, *args, **options):
        print(f'Need to import file {options["file"].name}')
