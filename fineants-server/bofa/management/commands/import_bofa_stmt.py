"""
Command to import data from a Bank of America statement in CSV form.
"""
import csv
from datetime import datetime

from bofa.models import Transaction
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from djmoney.money import Money


class Command(BaseCommand):
    help = "Reads a Bank of America statement CSV file and saves the transactions."

    def add_arguments(self, parser):
        parser.add_argument(
            "file",
            type=lambda f: open(f, newline=""),
            help="A Bank of America statement download in CSV format",
        )

    def handle(self, *args, **options):
        before_count = Transaction.objects.count()
        print(f"Transactions before import: {before_count}")
        for line in csv.reader(options["file"]):
            if line[0] != "Posted Date":
                trans_date = datetime.strptime(line[0], "%m/%d/%Y").date()
                ref_number = line[1]
                payee = line[2]
                addr = line[3]
                amount = Money(line[4], "USD")
                try:
                    if ref_number.strip() == "":
                        if payee.startswith("INTEREST CHARGED"):
                            Transaction.objects.create(
                                posted_on=trans_date,
                                ref_num=trans_date.strftime("%Y%m%d") + "_interest",
                                payee=payee,
                                amount=amount,
                            )
                        elif payee == "ANNUAL FEE":
                            Transaction.objects.create(
                                posted_on=trans_date,
                                ref_num=trans_date.strftime("%Y%m%d") + "_fee",
                                payee=payee,
                                amount=amount,
                            )
                        elif "DEBIT" in payee:
                            Transaction.objects.create(
                                posted_on=trans_date,
                                ref_num=trans_date.strftime("%Y%m%d") + "_fee",
                                payee=payee,
                                amount=amount,
                            )
                        else:
                            raise Exception(f"Missing refnum on line {line}")
                    else:
                        Transaction.objects.create(
                            posted_on=trans_date,
                            ref_num=ref_number,
                            payee=payee,
                            payee_addr=addr,
                            amount=amount,
                        )
                except IntegrityError:
                    print(f"skipping {ref_number}: already imported")
        after_count = Transaction.objects.count()
        print(f"Transactions after import: {after_count}")
        print(f"imported {after_count - before_count} transactions.")
