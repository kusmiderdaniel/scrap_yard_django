from django.contrib import admin
from .models import Receipt, ReceiptItem, EmptyItem

admin.site.register(Receipt)
admin.site.register(ReceiptItem)
admin.site.register(EmptyItem)