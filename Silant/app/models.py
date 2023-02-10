from django.db import models
from django.contrib.auth.models import User


class CarModel(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name}\n{self.description}"


class EngineModel(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name}\n{self.description}"


class TransmissionModel(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name}\n{self.description}"


class DrivingAxleModel(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name}\n{self.description}"


class SteeringAxleModel(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name}\n{self.description}"


class MaitenanceType(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name}\n{self.description}"


class MaitenanceProvider(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name}\n{self.description}"


class RepairMethod(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name}\n{self.description}"


class RepairUnit(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name}\n{self.description}"


class Manager(User):
    name = models.TextField()
    description = models.TextField()


class ServiceCompany(User):
    name = models.TextField()
    description = models.TextField()


class Client(User):
    name = models.TextField()
    description = models.TextField()


class Car(models.Model):
    class Meta:
        ordering = ["shipment_date"]

    serial_number = models.TextField()
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    engine_model = models.ForeignKey(EngineModel, on_delete=models.CASCADE)
    engine_serial_number = models.TextField()
    transmission_model = models.ForeignKey(TransmissionModel, on_delete=models.CASCADE)
    transmission_serial_number = models.TextField()
    driving_axle_model = models.ForeignKey(DrivingAxleModel, on_delete=models.CASCADE)
    driving_axle_serial_number = models.TextField()
    steering_axle_model = models.ForeignKey(SteeringAxleModel, on_delete=models.CASCADE)
    steering_axle_serial_number = models.TextField()
    contract_number = models.TextField()
    shipment_date = models.DateField()
    additional_equipment = models.TextField()
    buyer = models.ForeignKey(Client, on_delete=models.CASCADE)
    consignee = models.TextField()
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.serial_number


class Maitenance(models.Model):
    class Meta:
        ordering = ["date"]

    type = models.ForeignKey(MaitenanceType, on_delete=models.CASCADE)
    date = models.DateField()
    operating_time = models.IntegerField()
    contract_serial_number = models.TextField()
    contract_date = models.DateField()
    provider = models.ForeignKey(MaitenanceProvider, on_delete=models.DO_NOTHING)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE)


class Repair(models.Model):
    class Meta:
        ordering = ["issue_date"]

    issue_date = models.DateField()
    operating_time = models.IntegerField()
    unit = models.ForeignKey(RepairUnit, on_delete=models.DO_NOTHING)
    description = models.TextField()
    method = models.ForeignKey(RepairMethod, on_delete=models.DO_NOTHING)
    repair_parts = models.TextField()
    completion_date = models.DateField(null=True)
    # ⬇ completion_date - issue_date
    repair_time = models.IntegerField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE)

    def __repr__(self) -> str:
        return f"{self.issue_date}: {self.car} ({self.operating_time}) -- {self.serial_number}n\
            {self.description}n\
            {self.method}n\
            Parts needed: {self.repair_parts}n\
            {self.service_company}"
