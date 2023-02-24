from rest_framework import viewsets, permissions
from .serializers import *
from app.models import *
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponseForbidden
from django.http import Http404


# all methods
class CarViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.DjangoModelPermissionsOrAnonReadOnly,
    ]
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def retrieve(self, request, pk=None):
        try:
            q = Car.objects.get(serial_number=pk)
            s = None
            if (
                self.request.user.id == (q.buyer.id or q.service_company.id)
            ) or self.request.user.groups.filter(name="manager").exists():
                s = CarSerializer(q)
            else:
                s = LimitedCarSerializer(q)
        except Car.DoesNotExist:
            raise Http404
        return Response(s.data)

    def list(self, request, *args, **kwargs):
        try:
            q = None
            s = CarSerializer(q, many=True)
            if self.request.user.groups.filter(name="manager").exists():
                q = Car.objects.filter(buyer=request.user.id)
            elif self.request.user.groups.filter(name="client").exists():
                q = Car.objects.filter(buyer=request.user.id)
            elif self.request.user.groups.filter(name="service company").exists():
                q = Car.objects.filter(service_company=request.user.id)
            else:
                s = LimitedCarSerializer(q, many=True)
        except Car.DoesNotExist:
            raise Http404
        return Response(s.data)


class MaitenanceViewSet(viewsets.ModelViewSet):
    queryset = Maitenance.objects.all()
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = MaitenanceSerializer

    def retrieve(self, request, pk=None):
        try:
            q = Maitenance.objects.get(id=pk)
            s = None
            if (
                self.request.user.id == (q.car.buyer.id or q.service_company.id)
            ) or self.request.user.groups.filter(name="manager").exists():
                s = CarSerializer(q)
            else:
                Response(status=HttpResponseForbidden)
        except Maitenance.DoesNotExist:
            raise Http404
        return Response(s.data)

    def list(self, request, *args, **kwargs):
        try:
            q = None
            if self.request.user.groups.filter(name="client").exists():
                q = Maitenance.objects.filter(car__buyer=request.user.id)
            elif self.request.user.groups.filter(name="service company").exists():
                q = Maitenance.objects.filter(service_company=request.user.id)
            elif self.request.user.groups.filter(name="manager").exists():
                q = Maitenance.objects.all()
            else:
                return Response(status=HttpResponseForbidden)
            s = MaitenanceSerializer(q, many=True)
        except Maitenance.DoesNotExist:
            raise Http404
        return Response(s.data)


class RepairViewSet(viewsets.ModelViewSet):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer
    permission_classes = [permissions.DjangoModelPermissions]

    def retrieve(self, request, pk=None):
        try:
            q = Repair.objects.get(id=pk)
            s = None
            if (
                self.request.user.id == (q.car.buyer.id or q.service_company.id)
            ) or self.request.user.groups.filter(name="manager").exists():
                s = CarSerializer(q)
            else:
                Response(status=HttpResponseForbidden)
        except Repair.DoesNotExist:
            raise Http404
        return Response(s.data)

    def list(self, request, *args, **kwargs):
        try:
            q = Repair.objects.all()
            if self.request.user.groups.filter(name="client").exists():
                q = Repair.objects.filter(car__buyer=request.user.id)
            elif self.request.user.groups.filter(name="service company").exists():
                q = Repair.objects.filter(service_company=request.user.id)
            s = RepairSerializer(q, many=True)
        except Repair.DoesNotExist:
            raise Http404
        return Response(s.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.DjangoModelPermissions]

    @action(detail=False, methods=["get"])
    def current(self, request):
        try:
            q = None
            s = None
            if self.request.user.groups.filter(name="client").exists():
                print(self.request.user.groups.all())
                q = Client.objects.get(user__id=request.user.id)
                s = ClientSerializer(q, many=False)
            elif self.request.user.groups.filter(name="service company").exists():
                q = ServiceCompany.objects.get(user__id=request.user.id)
                s = ServiceSerializer(q, many=False)
            else:
                q = User.objects.get(id=request.user.id)
                s = UserSerializer(q, many=False)
        except User.DoesNotExist:
            raise Http404
        return Response(s.data)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = ServiceCompany.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class EngineModelViewSet(viewsets.ModelViewSet):
    queryset = EngineModel.objects.all()
    serializer_class = EngineModelSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class DrivingAxleModelViewSet(viewsets.ModelViewSet):
    queryset = DrivingAxleModel.objects.all()
    serializer_class = DrivingAxleModelSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class SteeringAxleModelViewSet(viewsets.ModelViewSet):
    queryset = SteeringAxleModel.objects.all()
    serializer_class = SteeringAxleModelSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class TransmissionModelViewSet(viewsets.ModelViewSet):
    queryset = TransmissionModel.objects.all()
    serializer_class = TransmissionModelSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class MaitenanceTypeViewSet(viewsets.ModelViewSet):
    queryset = MaitenanceType.objects.all()
    serializer_class = MaitenanceTypeSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class MaitenanceProviderViewSet(viewsets.ModelViewSet):
    queryset = MaitenanceProvider.objects.all()
    serializer_class = MaitenanceProviderSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class RepairMethodViewSet(viewsets.ModelViewSet):
    queryset = RepairMethod.objects.all()
    serializer_class = RepairMethodSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class RepairUnitViewSet(viewsets.ModelViewSet):
    queryset = RepairUnit.objects.all()
    serializer_class = RepairUnitSerializer
    permission_classes = [permissions.DjangoModelPermissions]
