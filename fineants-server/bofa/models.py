from django.db import models

from djmoney.models.fields import MoneyField


class Transaction(models.Model):
    """
    A specialized transaction model that matches the BofA download format, for initial imports.
    """
    # will we need date transaction actually occurred? Not part of downloaded stmt.
    posted_on = models.DateField('Transaction Date', help_text='Date transaction posted to account')
    ref_num = models.CharField('Reference Number', max_length=23, primary_key=True, help_text='Bank of America reference number')
    payee = models.CharField(max_length=256, help_text='Name of other party to transaction')
    payee_addr = models.CharField('Payee Address', max_length=512, help_text='Address (or contact info) of other party to transaction')
    amount = MoneyField(max_digits=19, decimal_places=4, default_currency='USD')
