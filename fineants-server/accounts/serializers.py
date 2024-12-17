from rest_framework import serializers

from .models import Bank, BankAccount, Transaction


class BankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bank
        fields = ['url', 'name', 'phone_number']


class BankAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['url', 'bank', 'account_number']


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ['url', 'account', 'amount', 'to_from', 'posted', 'memo', 'is_debit']
