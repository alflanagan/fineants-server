from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions

from .models import Bank, BankAccount, Transaction
from .serializers import BankSerializer, BankAccountSerializer, TransactionSerializer


class BankViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows banks to be viewed or edited.
    """
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [permissions.IsAuthenticated]

class BankAccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint for a specific account at a bank.
    """
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for a transaction.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
