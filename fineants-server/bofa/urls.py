from django.urls import path, include
from rest_framework import routers

from .views import TransactionViewSet

router = routers.DefaultRouter()
router.register(r'transaction', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
