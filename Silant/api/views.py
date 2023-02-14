from rest_framework import viewsets, permissions
from .permissions import *
from .serializers import *
from app.models import *

# all methods
class CarView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [
        CustomCarPermission,
    ]

    def get_queryset(self):
        return Car.objects.filter(id=self.kwargs["pk"])


class MaitenanceList(viewsets.ModelViewSet):
    queryset = Maitenance.objects.all()
    serializer_class = MaitenanceSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class RepairList(viewsets.ModelViewSet):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer
    permission_classes = [permissions.DjangoModelPermissions]
