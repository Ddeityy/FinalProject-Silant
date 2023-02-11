from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Manager(User):
    class Meta:
        verbose_name = "Менеджер"
        verbose_name_plural = "Менеджеры"

    name = models.TextField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class ServiceCompany(User):
    class Meta:
        verbose_name = "Сервисная организация"
        verbose_name_plural = "Сервисные организации"

    name = models.TextField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Client(User):
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    name = models.TextField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
