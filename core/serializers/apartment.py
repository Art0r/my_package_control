from core.models import Apartment, Resident
from rest_framework import serializers


class ResidentToApartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resident
        fields = ('id', 'name', 'email', 'phone',)


class ApartmentSerializer(serializers.HyperlinkedModelSerializer):
    resident = ResidentToApartmentSerializer(many=True, read_only=True)

    class Meta:
        model = Apartment
        fields = ('id', 'floor', 'number', 'resident', 'created_at', 'updated_at',)


class ApartmentToCondoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Apartment
        fields = ('id', 'floor', 'number',)

