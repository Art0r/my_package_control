from rest_framework.request import Request
from rest_framework.response import Response
from core.models import (Resident, Apartment, Package, Account, Condo)
from core.serializers import (CondoSerializer, AccountSerializer, ResidentSerializer,
                              ApartmentSerializer, PackageUpdateSerializer, PackageRetrieveSerializer,
                              PackageCreateSerializer)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from core.permissions import IsCondo


class AccountViewSet(GenericViewSet, RetrieveModelMixin,
                     UpdateModelMixin, DestroyModelMixin):
    queryset = Account.objects.all()
    http_method_names = ('get', 'put', 'post', 'delete')
    permission_classes = (IsAuthenticated,)
    serializer_class = AccountSerializer


class CondoViewSet(GenericViewSet, RetrieveModelMixin,
                   UpdateModelMixin, DestroyModelMixin):
    queryset = Condo.objects.all()
    http_method_names = ('get', 'put', 'post', 'delete')
    permission_classes = (IsAuthenticated,)
    serializer_class = CondoSerializer


class ResidentViewSet(ModelViewSet):
    queryset = Resident.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = ResidentSerializer
    permission_classes = (IsAuthenticated,)


class ApartmentViewSet(ModelViewSet):
    queryset = Apartment.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = ApartmentSerializer
    permission_classes = (IsAuthenticated,)


class PackageViewSet(ModelViewSet):
    queryset = Package.objects.all()
    authentication_classes = (TokenAuthentication,)
    http_method_names = ('get', 'put', 'post', 'delete')
    # permissions.IsAdminUse allow only users with is_staff = True
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'update':
            return PackageUpdateSerializer
        if self.action == 'create':
            return PackageCreateSerializer
        return PackageRetrieveSerializer

    @action(detail=False, methods=('get',), url_path="o")
    def custom(self, request: Request):
        return Response("Ola Mundo")
