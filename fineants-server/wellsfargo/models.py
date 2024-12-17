from django.db import models

from djmoney.models.fields import MoneyField


class WellsFargoStatement(models.Model):
    account = models.CharField('Account Number', max_length=20, blank=False)
    stmt_date = models.DateField('Statement Date', help_text='Date statement printed')
    beginning_bal = MoneyField('Beginning Balance', max_digits=19, decimal_places=4, default_currency='USD')
    ending_bal = MoneyField('Ending Balance', max_digits=19, decimal_places=4, default_currency='USD')
    total_debits = MoneyField('Withdrawals', max_digits=19, decimal_places=4, default_currency='USD')
    total_credits = MoneyField('Deposits', max_digits=19, decimal_places=4, default_currency='USD')

    class Meta:
        unique_together = ['account', 'stmt_date']

    def __str__(self):
        return f'Wells Fargo Statement (Account {self.account}): {self.stmt_date.strftime("%m/%d/%Y")}'


class WellsFargoStmtTrans(models.Model):
    """
    A specialized transaction model that matches the
    """

    uniq_id = models.CharField(
        'Unique ID', max_length=128, help_text='not provided by bank but created by us', blank=True
    )  # accepting blanks for migrations, should be blank=False in future
    posted_on = models.DateField('Transaction Date', help_text='Date transaction posted to account')
    check_num = models.CharField('Check Number', max_length=25, help_text='Check used for this trans', blank=True)
    description = models.CharField(max_length=500, help_text='Transaction description', blank=True)
    original_description = models.CharField(
        max_length=500, help_text='Raw description text sent by other party', blank=True
    )
    # deliberately requiring both fields below, even though one should be $0
    debit_amount = MoneyField(max_digits=19, decimal_places=4, default_currency='USD')
    credit_amount = MoneyField(max_digits=19, decimal_places=4, default_currency='USD')
    ending_balance = MoneyField(max_digits=19, decimal_places=4, default_currency='USD', null=True)
    labels = models.CharField(max_length=500, help_text='rarely-used extra field')
    notes = models.CharField(max_length=500, help_text='Notes about transaction from bank')
