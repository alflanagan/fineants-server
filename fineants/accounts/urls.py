from django.db.models.manager import BaseManager
from django.urls import path, include
from rest_framework import routers

from .views import BankViewSet, BankAccountViewSet, TransactionViewSet

router = routers.DefaultRouter()
router.register(r'bank', BankViewSet)
router.register(r'bankaccount', BankAccountViewSet)
router.register(r'transaction', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
