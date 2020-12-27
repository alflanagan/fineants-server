from django.db import models

# Create your models here.


class Bank(models.Model):
    """A financial institution of some sort."""
    name = models.CharField(max_length=200, primary_key=True)
    phone_number = models.CharField(max_length=20)


class BankAccount(models.Model):
    bank = models.ForeignKey(
        Bank, on_delete=models.PROTECT, help_text="Financial institution holding the account")
    account_number = models.CharField(max_length=200)

    class Meta:
        unique_together = ('bank', 'account_number')


class Transaction(models.Model):
    """Anything that changes the balance of an account."""
    account = models.ForeignKey(BankAccount, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=15,
        decimal_places=2)  # some accounts may require 4?
    to_from = models.CharField(max_length=100)
    posted = models.DateTimeField()
    memo = models.TextField()
    is_debit = models.BooleanField(null=False)

    class Meta:
        unique_together = ('account', 'posted')
