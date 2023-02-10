from django.contrib import admin
from .models import *

admin.site.register(Car)
admin.site.register(CarDetail)
admin.site.register(Maitenance)
admin.site.register(MaitenanceDetail)
admin.site.register(Repair)
admin.site.register(RepairDetail)
admin.site.register(Client)
admin.site.register(ServiceCompany)
