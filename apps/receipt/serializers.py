from rest_framework import serializers

from .models import Receipt, ReceiptItem, EmptyItem

class ReceiptItemSerializer(serializers.ModelSerializer):   
    class Meta:
        model = ReceiptItem
        read_only_fields = (
            "receipt",
        )
        fields = (
            "id",
            "source_id",
            "item_num",
            "name",
            "item_code",
            "quantity",
            "buy_price",
            "sell_price",
            "gross_amount",
        )
    
class ReceiptEmptyItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmptyItem
        read_only_fields = (
            "receipt",
        )
        fields = (
            "id",
            "item_num",
        )

class ReceiptSerializer(serializers.ModelSerializer):   
    receipt_items = ReceiptItemSerializer(many=True)
    receipt_empty_items = ReceiptEmptyItemSerializer(many=True)

    class Meta:
        model = Receipt
        read_only_fields = (
            "team",
            "created_at",
            "created_by",
            "modified_at",
            "modified_by",
        ),
        fields = (
            "id",
            "receipt_number",
            "date",
            "client",
            "client_name",
            "client_email",
            "client_doc_number",
            "client_address1",
            "client_zipcode",
            "client_place",
            "gross_amount",
            "total_quantity",
            "receipt_items",
            "receipt_empty_items"
        )
    
    def create(self, validated_data):
        items_data = validated_data.pop('receipt_items')
        empty_items_data = validated_data.pop('receipt_empty_items')
        receipt = Receipt.objects.create(**validated_data)

        for item in items_data:
            ReceiptItem.objects.create(receipt=receipt, **item)

        for emptyItem in empty_items_data:
            EmptyItem.objects.create(receipt=receipt, **emptyItem)
        
        return receipt
    
    def update(self, instance, validated_data):
        # Update the simple fields
        instance.receipt_number = validated_data.get('receipt_number', instance.receipt_number)
        instance.date = validated_data.get('date', instance.date)
        instance.client = validated_data.get('client', instance.client)
        instance.client_name = validated_data.get('client_name', instance.client_name)
        instance.client_email = validated_data.get('client_email', instance.client_email)
        instance.client_doc_number = validated_data.get('client_doc_number', instance.client_doc_number)
        instance.client_address1 = validated_data.get('client_address1', instance.client_address1)
        instance.client_zipcode = validated_data.get('client_zipcode', instance.client_zipcode)
        instance.client_place = validated_data.get('client_place', instance.client_place)
        instance.gross_amount = validated_data.get('gross_amount', instance.gross_amount)
        instance.total_quantity = validated_data.get('total_quantity', instance.gross_amount)

        # Update receipt items
        items_data = validated_data.get('receipt_items', [])
        empty_items_data = validated_data.get('receipt_empty_items', [])
        instance.receipt_items.all().delete()  # Remove existing items
        instance.receipt_empty_items.all().delete() # Remove existing empty items

        for item_data in items_data:
            ReceiptItem.objects.create(receipt=instance, **item_data)

        for emptyItem in empty_items_data:
            EmptyItem.objects.create(receipt=instance, **emptyItem)

        instance.save()

        return instance