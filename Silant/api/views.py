from rest_framework import viewsets, permissions, status
from .serializers import *
from app.models import *
from rest_framework.response import Response
from django.http import Http404


# all methods
class CarView(viewsets.ModelViewSet):
    permission_classes = [
        permissions.DjangoModelPermissionsOrAnonReadOnly,
    ]
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def retrieve(self, request, pk=None):
        q = Car.objects.get(id=pk)
        s = CarSerializer(q)
        if (
            self.request.user.id == (q.buyer.id or q.service_company)
        ) or self.request.user.groups.filter(name="manager").exists():
            pass
        else:
            s = LimitedCarSerializer(q)
        return Response(s.data)

    def list(self, request, *args, **kwargs):
        q = Car.objects.all()
        s = CarSerializer(q, many=True)
        if self.request.user.is_anonymous:
            s = LimitedCarSerializer(q, many=True)
        elif self.request.user.groups.filter(name="client").exists():
            q = Car.objects.filter(buyer=request.user.id)
        elif self.request.user.groups.filter(name="service company").exists():
            q = Car.objects.filter(service_company=request.user.id)
        return Response(s.data)


class MaitenanceList(viewsets.ModelViewSet):
    queryset = Maitenance.objects.all()
    permission_classes = [
        permissions.DjangoObjectPermissions,
        permissions.DjangoModelPermissions,
    ]


class RepairList(viewsets.ModelViewSet):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer
    permission_classes = [permissions.DjangoModelPermissions]
