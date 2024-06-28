from uuid import UUID
from django.http import HttpRequest, JsonResponse
from rest_framework.response import Response
from core.models import Resident, Apartment, Package
from core.serializers import ResidentSerializer, ApartmentSerializer, \
    PackageCreateSerializer, PackageRetrieveSerializer, PackageUpdateSerializer
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication


class ResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = ResidentSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = ApartmentSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    authentication_classes = (TokenAuthentication,)
    http_method_names = ('get', 'put', 'post', 'delete')
    # permissions.IsAdminUse allow only users with is_staff = True
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def get_serializer_class(self):
        if self.action == 'update':
            return PackageUpdateSerializer
        if self.action == 'create':
            return PackageCreateSerializer
        return PackageRetrieveSerializer

    @action(detail=False, methods=('get',), url_path="o")
    def custom(self, request: HttpRequest):
        return Response("Ola Mundo")
