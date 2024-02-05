from rest_framework import serializers

from .models import Client
from apps.receipt.models import Receipt

class ClientReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = (
            "id",
            "date",
            "receipt_number",
            "gross_amount"
        )

class ClientSerializer(serializers.ModelSerializer):
    receipts = ClientReceiptSerializer(many=True, required=False)

    class Meta:
        model = Client
        read_only_fields = (
            'created_at',
            'created_by',
            'modified_at',
            'modified_by',
        )
        fields = (
            'id',
            'name',
            'email',
            'doc_number',
            'address1',
            'zipcode',
            'place',
            'receipts',
        )
    
    def update(self, instance, validated_data):
        # Update Client instance fields
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.doc_number = validated_data.get('doc_number', instance.doc_number)
        instance.address1 = validated_data.get('address1', instance.address1)
        instance.zipcode = validated_data.get('zipcode', instance.zipcode)
        instance.place = validated_data.get('place', instance.place)
        instance.save()

        # Update associated Receipt instances
        receipts_data = validated_data.get('receipts', [])

        for receipt_data in receipts_data:
            receipt_id = receipt_data.get('id', None)
            
            if receipt_id:
                # If receipt_id is present, update the existing Receipt instance
                receipt_instance = instance.receipts.filter(id=receipt_id).first()

                receipt_data.client_name = instance.name

                if receipt_instance:
                    # Update the existing receipt
                    receipt_serializer = ClientReceiptSerializer(
                        receipt_instance, data=receipt_data, partial=True
                    )

                    if receipt_serializer.is_valid():
                        receipt_serializer.save()

        return instance