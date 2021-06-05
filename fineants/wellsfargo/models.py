from django.db import models
from djmoney.money import Money
from djmoney.models.fields import MoneyField


class WellsFargoStmtTrans(models.Model):
    """
    A specialized transaction model that matches the
    """
    posted_on = models.DateField('Transaction Date', help_text='Date transaction posted to account')
    check_num = models.CharField('Check Number', max_length=25, help_text='Check used for this trans')
    description = models.CharField(max_length=500, help_text='Transaction description')
    dep_amount = MoneyField(max_digits=19, decimal_places=4, default_currency='USD')
    with_amount = MoneyField(max_digits=19, decimal_places=4, default_currency='USD')
    ending_balance = MoneyField(max_digits=19, decimal_places=4, default_currency='USD')
