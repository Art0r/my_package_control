from core.serializers.package import PackageRetrieveSerializer
from core.models import Resident, Apartment
from rest_framework import serializers


class ApartmentToResidentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Apartment
        fields = ('id', 'floor', 'number',)


class ResidentSerializer(serializers.HyperlinkedModelSerializer):
    package = PackageRetrieveSerializer(many=True, read_only=True)
    apto = ApartmentToResidentSerializer(many=False, read_only=True)

    class Meta:
        model = Resident
        fields = ('id', 'name', 'email', 'phone', 'apto', 'package', 'created_at', 'updated_at',)
