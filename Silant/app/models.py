from django.db import models
from django.contrib.auth.models import User


class Detail(models.Model):
    name = models.TextField()
    title = models.TextField()
    description = models.TextField()


class Car(models.Model):
    serial_number = models.TextField()
    model = models.ForeignKey(Detail)
    engine_model = models.ForeignKey(Detail)
    engine_serial_number = models.TextField()
    transmission_model = models.ForeignKey(Detail)
    transmission_serial_number = models.TextField()
    drive_axle_model = models.ForeignKey(Detail)
    drive_axle_serial_number = models.TextField()
    steering_axle_model = models.ForeignKey(Detail)
    steering_axle_serial_number = models.TextField()
    contract_number = models.TextField()
    shipment_date = models.DateTimeField()
    buyer = models.TextField()
    buyer_adress = models.TextField()
    additional_equipment = models.TextField()
    client = models.ForeignKey(User)
    service_company = models.ForeignKey(User)


class Maitenance(models.Model):
    type = models.ForeignKey(Detail)
    date = models.DateTimeField()
    operating_time = models.IntegerField()
    contract_serial_number = models.TextField()
    contract_date = models.DateTimeField()
    provider = models.ForeignKey(Detail)
    car = models.ForeignKey(Car)
    service_company = models.ForeignKey(User)


class Reclamation(models.Model):
    issue_date = models.DateTimeField()
    operating_time = models.IntegerField()
    serial_number = models.ForeignKey(Detail)
    description = models.TextField()
    method = models.ForeignKey(Detail)
    repair_parts = models.TextField()
    completion_date = models.DateTimeField()
    # ⬇ completion_date - issue_date
    repair_time = models.IntegerField()
    car = models.ForeignKey(Car)
    service_company = models.ForeignKey(User)
