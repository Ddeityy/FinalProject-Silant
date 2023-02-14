from rest_framework import serializers
from app.models import *
from rest_framework.exceptions import PermissionDenied

unauthorized_fields = [
    "shipment_date",
    "buyer",
    "consignee",
    "delivery_adress",
    "additional_equipment",
    "service_company",
]


class DynamicCarSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        request = kwargs.get("context", {}).get("request")
        super().__init__(*args, **kwargs)
        if request.user.is_anonymous:
            for field in unauthorized_fields:
                self.fields.pop(field)


class CarSerializer(DynamicCarSerializer):
    def create(self, *args, **kwargs):
        request = kwargs.get("context", {}).get("request")
        request.user.groups.filter(name="client").exists()

    class Meta:
        model = Car
        fields = "__all__"


class MaitenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maitenance
        fields = ["__all__"]


class RepairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repair
        fields = ["__all__"]
