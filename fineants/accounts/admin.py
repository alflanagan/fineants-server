from django.contrib import admin
from .models import Bank, BankAccount, Transaction

admin.site.register(Bank)
admin.site.register(BankAccount)
admin.site.register(Transaction)