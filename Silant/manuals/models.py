from django.db import models


class CarModel(models.Model):
    class Meta:
        verbose_name = "Модель техники"
        verbose_name_plural = "Модели техники"

    name = models.TextField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class EngineModel(models.Model):
    class Meta:
        verbose_name = "Модель двигателя"
        verbose_name_plural = "Модели двигателей"

    name = models.TextField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class TransmissionModel(models.Model):
    class Meta:
        verbose_name = "Модель трансмиссии"
        verbose_name_plural = "Модели трансмиссий"

    name = models.TextField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class DrivingAxleModel(models.Model):
    class Meta:
        verbose_name = "Модель ведущего моста"
        verbose_name_plural = "Модели ведущих мостов"

    name = models.TextField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class SteeringAxleModel(models.Model):
    class Meta:
        verbose_name = "Модель управляемого моста"
        verbose_name_plural = "Модели управляемых мостов"

    name = models.TextField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class MaitenanceType(models.Model):
    class Meta:
        verbose_name = "Вид ТО"
        verbose_name_plural = "Виды ТО"

    name = models.TextField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class MaitenanceProvider(models.Model):
    class Meta:
        verbose_name = "Организация, проводившая ТО"
        verbose_name_plural = "Организации, проводившие ТО"

    name = models.TextField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class RepairMethod(models.Model):
    class Meta:
        verbose_name = "Способ восстановления"
        verbose_name_plural = "Способы восстановления"

    name = models.TextField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class RepairUnit(models.Model):
    class Meta:
        verbose_name = "Узел отказа"
        verbose_name_plural = "Узлы отказа"

    name = models.TextField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
