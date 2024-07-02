from django.http import HttpRequest, JsonResponse
from rest_framework.response import Response
from core.models import Resident, Apartment, Package, Account
from core.serializers import ResidentSerializer, ApartmentSerializer, \
    PackageCreateSerializer, PackageRetrieveSerializer, PackageUpdateSerializer, CondoSerializer
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class CondoViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.filter(type=Account.Types.CONDO)
    http_method_names = ('get', 'put', 'post', 'delete')
    permission_classes = (permissions.AllowAny,)
    serializer_class = CondoSerializer


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


class TokenHandling(APIView):
    def post(self, request: Request, *args, **kwargs):

        data = request.data
        email = data.get('email')
        password = data.get('password')

        user = authenticate(request, username=email, password=password)

        if user is None:
            return Response(status=status.HTTP_403_FORBIDDEN)

        token, _ = Token.objects.get_or_create(user=user)

        return JsonResponse({"res": token.key})
