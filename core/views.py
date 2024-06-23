from core.models import Resident, Apartment, Package
from core.serializers import ResidentSerializer, ApartmentSerializer, \
    PackageSerializer, PackageRetrieveSerializer
from rest_framework import permissions, viewsets, generics


class ResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer
    permission_classes = (permissions.AllowAny,)


class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = (permissions.AllowAny,)


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    permission_classes = (permissions.AllowAny,)

    def get_serializer_class(self):
        if self.action in ['create', 'update',]:
            return PackageSerializer
        return PackageRetrieveSerializer
