import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Silant.settings")
from django import setup

setup()
import random
import string
from app.models import *
from users.models import *
from manuals.models import *
from django.contrib.auth.models import User
from openpyxl import load_workbook


wb = load_workbook(filename="data.xlsx")
print(wb.sheetnames)
car = wb["машины"]
mtn = wb["ТО output"]
rec = wb["рекламация output"]
car_usr = range(4, 14)
rep_range = range(3, 15)
mtn_range = range(2, 38)


def init_superuser():
    try:
        User.objects.create_superuser(username="admin", password="admin")
        print("Superuser created")
    except Exception as e:
        print(e)


def random_string():
    characters = string.ascii_letters + string.digits + string.punctuation
    result = "".join(random.choice(characters) for i in range(12))
    return result


def init_manuals_and_users():
    # car parts
    for i in car_usr:
        try:
            CarModel.objects.create(name=car[f"B{i}"].value)
        except Exception as e:
            print(e)
        try:
            EngineModel.objects.create(name=car[f"D{i}"].value)
        except Exception as e:
            print(e)
        try:
            TransmissionModel.objects.create(name=car[f"F{i}"].value)
        except Exception as e:
            print(e)
        try:
            DrivingAxleModel.objects.create(name=car[f"H{i}"].value)
        except Exception as e:
            print(e)
        try:
            SteeringAxleModel.objects.create(name=car[f"J{i}"].value)
        except Exception as e:
            print(e)
        try:
            Client.objects.create(
                username=random_string().lower(),
                password=random_string(),
                name=car[f"M{i}"].value,
            )
        except Exception as e:
            print(e)
        try:
            ServiceCompany.objects.create(
                username=random_string().lower(),
                password=random_string(),
                name=car[f"Q{i}"].value,
            )
        except Exception as e:
            print(e)

    for i in rep_range:
        try:
            RepairUnit.objects.create(name=rec[f"D{i}"].value)
        except Exception as e:
            print(e)
        try:
            RepairMethod.objects.create(name=rec[f"F{i}"].value)
        except Exception as e:
            print(e)

    # maitenance
    for i in mtn_range:
        try:
            MaitenanceType.objects.create(name=mtn[f"B{i}"].value)
        except Exception as e:
            print(e)
        try:
            MaitenanceProvider.objects.create(name=mtn[f"G{i}"].value)
        except Exception as e:
            print(e)


def init_cars():
    try:
        for i in car_usr:
            Car.objects.create(
                contract_number=car[f"A{i}"].value,
                model=CarModel.objects.get(name=car[f"B{i}"].value),
                serial_number=car[f"C{i}"].value,
                engine_model=EngineModel.objects.get(name=car[f"D{i}"].value),
                engine_serial_number=car[f"E{i}"].value,
                transmission_model=TransmissionModel.objects.get(
                    name=car[f"F{i}"].value
                ),
                transmission_serial_number=car[f"G{i}"].value,
                driving_axle_model=DrivingAxleModel.objects.get(
                    name=car[f"H{i}"].value
                ),
                driving_axle_serial_number=car[f"I{i}"].value,
                steering_axle_model=SteeringAxleModel.objects.get(
                    name=car[f"J{i}"].value
                ),
                steering_axle_serial_number=car[f"K{i}"].value,
                shipment_date=car[f"L{i}"].value,
                buyer=Client.objects.get(name=car[f"M{i}"].value),
                consignee=car[f"N{i}"].value,
                delivery_adress=car[f"O{i}"].value,
                additional_equipment=car[f"P{i}"].value,
                service_company=ServiceCompany.objects.get(name=car[f"Q{i}"].value),
            )
    except Exception as e:
        print(e)


def init_maitenance():
    for i in mtn_range:
        car = Car.objects.get(serial_number=mtn[f"A{i}"].value)
        if mtn[f"G{i}"].value == "самостоятельно":
            p = MaitenanceProvider.objects.get(id=4)
            s = True
        else:
            p = MaitenanceProvider.objects.get(name=mtn[f"G{i}"].value)
            s = False
        try:
            Maitenance.objects.create(
                type=MaitenanceType.objects.get(name=mtn[f"B{i}"].value),
                date=mtn[f"C{i}"].value,
                operating_time=mtn[f"D{i}"].value,
                contract_serial_number=mtn[f"E{i}"].value,
                contract_date=mtn[f"F{i}"].value,
                self_maitenance=s,
                provider=p,
                car=car,
                service_company=car.service_company,
            )
        except Exception as e:
            print(e)


def init_repairs():
    for i in rep_range:
        try:
            car = Car.objects.get(serial_number=rec[f"A{i}"].value)
            Repair.objects.create(
                issue_date=rec[f"B{i}"].value,
                operating_time=rec[f"C{i}"].value,
                unit=RepairUnit.objects.get(name=rec[f"D{i}"].value),
                description=rec[f"E{i}"].value,
                method=RepairMethod.objects.get(name=rec[f"F{i}"].value),
                repair_parts=rec[f"G{i}"].value,
                completion_date=rec[f"H{i}"].value,
                repair_time=int((rec[f"H{i}"].value - rec[f"B{i}"].value).days),
                car=car,
                service_company=car.service_company,
            )
        except Exception as e:
            print(e)


import logging

logger = logging.getLogger()

# manager
def init_manager():
    try:
        Manager.objects.create(username="manager", password="password", name="Менеджер")
        print("Manager created")
    except Exception as e:
        logger.exception(repr(e))


init_superuser()
init_manuals_and_users()
init_manager()
init_cars()
init_repairs()
init_maitenance()
