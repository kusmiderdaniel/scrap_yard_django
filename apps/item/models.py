import decimal

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='created_categories', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    category_name = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    item_code = models.CharField(max_length=6, null=True)
    quantity = models.FloatField(default=1.00)
    buy_price = models.DecimalField(max_digits=6, decimal_places=2)
    sell_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    created_by = models.ForeignKey(User, related_name='created_items', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return '%s' % self.name