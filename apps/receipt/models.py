from datetime import timedelta, datetime

from django.contrib.auth.models import User
from django.db import models

from apps.client.models import Client
from apps.team.models import Team

class Receipt(models.Model):
    receipt_number = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)
    client_email = models.CharField(max_length=255, null=True)
    client_doc_number = models.CharField(max_length=255, blank=True, null=True)
    client_address1 = models.CharField(max_length=255, blank=True, null=True)
    client_zipcode = models.CharField(max_length=255, blank=True, null=True)
    client_place = models.CharField(max_length=255, blank=True, null=True)
    gross_amount = models.DecimalField(max_digits=6, decimal_places=2)
    total_quantity = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    team = models.ForeignKey(Team, related_name='receipts', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='receipts', on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='created_receipts', on_delete=models.CASCADE)
    modified_by = models.ForeignKey(User, related_name='modified_receipts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s' % self.receipt_number

class ReceiptItem(models.Model):
    source_id = models.IntegerField(default=-1)
    receipt = models.ForeignKey(Receipt, related_name="receipt_items", on_delete=models.CASCADE, null=True)
    item_num = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    item_code = models.CharField(max_length=6, null=True)
    quantity = models.FloatField(default=1.00)
    buy_price = models.DecimalField(max_digits=6, decimal_places=2)
    sell_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    gross_amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return '%s' % self.name
    
class EmptyItem(models.Model):
    receipt = models.ForeignKey(Receipt, related_name="receipt_empty_items", on_delete=models.CASCADE, null=True)
    item_num = models.IntegerField(default=0)