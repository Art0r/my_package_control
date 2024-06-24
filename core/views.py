from django.http import HttpRequest
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from core.models import Resident, Apartment, Package
from core.serializers import ResidentSerializer, ApartmentSerializer, \
    PackageCreateUpdateSerializer, PackageRetrieveSerializer, ValidatePackageSerializer
from rest_framework import permissions, viewsets,generics
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
        if self.action in ('create', 'update',):
            return PackageCreateUpdateSerializer
        return PackageRetrieveSerializer

    @action(detail=False, methods=('get',), url_path="o")
    def custom(self, request: HttpRequest):

        self.serializer_class = ValidatePackageSerializer

        return Response("Ola Mundo")


class ValidateViewSet(generics.UpdateAPIView):
    queryset = Package.objects.all()
    serializer_class = ValidatePackageSerializer
    permission_classes = (permissions.AllowAny,)
    http_method_names = ('put',)