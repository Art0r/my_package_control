from uuid import UUID
from django.http import HttpRequest, JsonResponse
from rest_framework.response import Response
from core.models import Resident, Apartment, Package
from core.serializers import ResidentSerializer, ApartmentSerializer, \
    PackageCreateSerializer, PackageRetrieveSerializer, PackageUpdateSerializer
from rest_framework import permissions, viewsets
from rest_framework.decorators import action


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
    http_method_names = ('get', 'put', 'post', 'delete')
    permission_classes = (permissions.AllowAny,)

    def get_serializer_class(self):
        if self.action == 'update':
            return PackageUpdateSerializer
        if self.action == 'create':
            return PackageCreateSerializer
        return PackageRetrieveSerializer

    @action(detail=False, methods=('get',), url_path="o")
    def custom(self, request: HttpRequest):
        return Response("Ola Mundo")
