from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ReceiptViewSet, ReceiptItemViewSet, ReceiptEmptyItemViewSet, generate_pdf, generate_receipts

router = DefaultRouter()
router.register("receipts", ReceiptViewSet, basename="receipts")
router.register("receipt-empty-items", ReceiptEmptyItemViewSet, basename="receipt-empty-items")
router.register("receipt-items", ReceiptItemViewSet, basename="receipt-items")

urlpatterns = [
    path('', include(router.urls)),
    path('receipts/<int:receipt_id>/generate_pdf/', generate_pdf, name='generate_pdf'),
    path('generate_receipts/', generate_receipts, name='generate_receipts'),
]