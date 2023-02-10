from django.db import models
from django.contrib.auth.models import User


class Manual(models.Model):
    ENTITIES = [
        (
            "Машины",
            (
                ("model", "Модель техники"),
                ("engine", "Модель двигателя"),
                ("transmission", "Модель трансмиссии"),
                ("driving axle", "Модель ведущего моста"),
                ("steering axle", "Модель управляемого моста"),
            ),
        ),
        (
            "ТО",
            (
                ("type", "Вид ТО"),
                ("provider", "Компания ТО"),
            ),
        ),
        (
            "Рекламации",
            (
                ("serial", "Характер отказа"),
                ("type", "Способ восстановления"),
            ),
        ),
    ]
    entity = models.TextField(choices=ENTITIES)
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"{self.entity}\n{self.name}\n{self.description}"


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
    model = models.ForeignKey(
        Manual, related_name="car_model", on_delete=models.CASCADE
    )
    engine_model = models.ForeignKey(
        Manual, related_name="car_engine_model", on_delete=models.CASCADE
    )
    engine_serial_number = models.TextField()
    transmission_model = models.ForeignKey(
        Manual, related_name="car_transmission_model", on_delete=models.CASCADE
    )
    transmission_serial_number = models.TextField()
    driving_axle_model = models.ForeignKey(
        Manual, related_name="car_driving_axle_model", on_delete=models.CASCADE
    )
    driving_axle_serial_number = models.TextField()
    steering_axle_model = models.ForeignKey(
        Manual, related_name="car_steering_axle_model", on_delete=models.CASCADE
    )
    steering_axle_serial_number = models.TextField()
    contract_number = models.TextField()
    shipment_date = models.DateField()
    additional_equipment = models.TextField()
    buyer = models.ForeignKey(Client, on_delete=models.CASCADE)
    consignee = models.TextField()
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.serial_number


class CarDetail(models.Model):
    entity_name = models.ForeignKey(Car, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()


class Maitenance(models.Model):
    class Meta:
        ordering = ["date"]

    type = models.ForeignKey(
        Manual, related_name="maitenance_type", on_delete=models.CASCADE
    )
    date = models.DateField()
    operating_time = models.IntegerField()
    contract_serial_number = models.TextField()
    contract_date = models.DateField()
    provider = models.ForeignKey(
        Manual, related_name="maitenance_provider", on_delete=models.DO_NOTHING
    )
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE)


class MaitenanceDetail(models.Model):
    entity_name = models.ForeignKey(Maitenance, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()


class Repair(models.Model):
    class Meta:
        ordering = ["issue_date"]

    issue_date = models.DateField()
    operating_time = models.IntegerField()
    serial_number = models.ForeignKey(
        Manual, related_name="repair_serial_number", on_delete=models.DO_NOTHING
    )
    description = models.TextField()
    method = models.ForeignKey(
        Manual, related_name="repair_method", on_delete=models.DO_NOTHING
    )
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


class RepairDetail(models.Model):
    entity_name = models.ForeignKey(Repair, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
