from django.db import models
from django.contrib.auth.models import User

class Manual(models.Model):
    pass



class Car(models.Model):
    serial_number = models.TextField()
    model = models.ForeignKey(Manual)
    engine_model = models.ForeignKey(Manual)
    engine_serial_number = models.TextField()
    transmission_model = models.ForeignKey(Manual)
    transmission_serial_number = models.TextField()
    drive_axle_model = models.ForeignKey(Manual)
    drive_axle_serial_number = models.TextField()
    steering_axle_model = models.ForeignKey(Manual)
    steering_axle_serial_number = models.TextField()
    contract_number = models.TextField()
    shipment_date = models.DateTimeField()
    buyer = models.TextField()
    buyer_adress = models.TextField()
    additional_equipment = models.TextField()
    client = models.ForeignKey(User)
    service_company = models.ForeignKey(User)
    
class Maitenance(models.Model):
    type = models.ForeignKey(Manual)
    date = models.DateTimeField()
    operating_time = models.IntegerField() 
    contract_serial_number = models.TextField()
    contract_date = models.DateTimeField()
    provider = models.ForeignKey(Manual)
    car = models.ForeignKey(Car)
    service_company = models.ForeignKey(User)
    
class Reclamation(models.Model):
    issue_date = models.DateTimeField()
    operating_time = models.IntegerField()
    serial_number = models.ForeignKey(Manual)
    description = models.TextField()
    method = models.ForeignKey(Manual)
    repair_parts = models.TextField()
    completion_date = models.DateTimeField()
    # ⬇ completion_date - issue_date
    repair_time = models.IntegerField()
    car = models.ForeignKey(Car)
    service_company = models.ForeignKey(User)

