from rest_framework import serializers
from app.models import *

authorized_fields = [
    "shipment_date",
    "buyer",
    "consignee",
    "delivery_adress",
    "additional_equipment",
    "service_company",
]


class LimitedCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in authorized_fields:
            self.fields.pop(field)


class CarSerializer(serializers.ModelSerializer):
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
