from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ReceiptViewSet, ReceiptEmptyItemViewSet, generate_pdf

router = DefaultRouter()
router.register("receipts", ReceiptViewSet, basename="receipts")
router.register("receipt-empty-items", ReceiptEmptyItemViewSet, basename="receipt-empty-items")

urlpatterns = [
    path('', include(router.urls)),
    path('receipts/<int:receipt_id>/generate_pdf/', generate_pdf, name='generate_pdf'),
]