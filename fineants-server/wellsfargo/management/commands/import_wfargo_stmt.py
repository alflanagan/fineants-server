"""
Command to import data from a Wells Fargo statement PDF.
"""
import argparse
import re
from datetime import datetime

from django.core.management.base import BaseCommand

from djmoney.money import Money

from imports.pdffuncs import get_text
from wellsfargo.models import WellsFargoStatement


def chomp(a_line):
    while a_line.endswith("\n"):
        a_line = a_line[:-1]
    return a_line


MONTHS = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}


def to_money(amount):
    """
    Given an string with some monetary amount, clean it up as necessary and return the equivalent
    `Money` object.
    """
    # Money doesn't like commas
    amount = amount.replace(',', '').replace('$', '')
    amount = amount.strip()
    neg = False
    if amount.startswith('-'):
        neg = True
        # account for spaces between minus and number
        amount = amount[1:].strip()
    result = Money(amount, 'USD')
    return result if not neg else -result


def get_activity_totals(lines):
    matcher = re.compile(r'([- $]*\W*[\d,.]+)')
    assert len(lines) == 8
    beginning = deposits = withdrawals = ending = None
    match = matcher.match(lines[4])
    if match:
        beginning = to_money(match.group(1))
    match = matcher.match(lines[5])
    if match:
        deposits = to_money(match.group(1))
    match = matcher.match(lines[6])
    if match:
        withdrawals = to_money(match.group(1))
    match = matcher.match(lines[7])
    if match:
        ending = to_money(match.group(1))
    return beginning, deposits, withdrawals, ending


class Command(BaseCommand):
    help = "Reads a Wells Fargo Statement PDF and saves the transactions."

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument(
            "pdf_file",
            type=lambda f: open(f, mode="rb"),
            help="A Wells Fargo statement download in PDF format",
        )

    def handle(self, *args, **options):
        """
        Opens a PDF file, extracts the text, adds transactions to `WellsFargoStmtTrans` table.
        """
        account = year = month = day_of_month = end = withdrawals = dep = beginning = None
        transtart = transend = 0
        with options["pdf_file"] as pdf:
            lines = get_text(pdf)

        lines = [chomp(line) for line in lines]
        for index, line in enumerate(lines):
            if "Custom Management® Checking" in line:
                search_index = index + 1
                for date_line in lines[search_index:]:
                    m = re.search(r"(?P<month>\w+)\W+(?P<day_of_month>\d+),\W+(?P<year>\d{4})", date_line)
                    if m:
                        day_of_month, month, year = m.group("day_of_month"), m.group("month"), m.group("year")
                        break

            if line == "Statement period activity summary":
                beginning, dep, withdrawals, end = get_activity_totals(lines[index + 1:index + 9])

            if line.startswith('Account number'):
                match = re.match(r'Account number:\W+(\w+)', line)
                if match:
                    account = match.group(1)

            if line.startswith('Transaction History') and transtart == 0:
                transtart = index+1

            if line.startswith('Totals') and transend == 0:
                transend = index

        # for now, we want to raise a nasty error if can't read date
        stmt = WellsFargoStatement(
            account=account,
            beginning_bal=beginning,
            stmt_date=datetime(int(year), int(MONTHS[month]), int(day_of_month)),
            ending_bal=end,
            total_debits=withdrawals,
            total_credits=dep,
            start_date=transtart,

        )
        print(stmt)
        print(stmt.beginning_bal, stmt.total_debits, stmt.total_credits, stmt.ending_bal)
