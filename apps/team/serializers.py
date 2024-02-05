from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        read_only_fields = (
            "created_by",
        )
        fields = (
            "id",
            "name",
            "owner_name",
            "short_name",
            "org_number",
            "org_number2",
            "phone_number",
            "email",
            "address1",
            "zipcode",
            "place"
        )