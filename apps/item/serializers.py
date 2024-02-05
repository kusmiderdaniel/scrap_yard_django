from rest_framework import serializers

from .models import Item, Category

class CategorySerializer(serializers.ModelSerializer):   
    class Meta:
        model = Category
        read_only_fields = (
            "created_by",
            "created_at",
        )
        fields = (
            "id",
            "name",
        )

class ItemSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Item
        read_only_fields = (
            "created_by",
            "created_at",
        )
        fields = (
            "id",
            "category",
            "category_name",
            "name",
            "item_code",
            "quantity",
            "buy_price",
            "sell_price",
        )