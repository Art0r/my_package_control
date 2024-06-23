from django.http import HttpRequest

from core.models import Resident, Apartment, Package
from rest_framework import serializers


class ResidentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Resident
        fields = ('id', 'name', 'email', 'apto', 'created_at', 'updated_at',)


class ApartmentSerializer(serializers.HyperlinkedModelSerializer):
    resident = ResidentSerializer(many=True, read_only=True)

    class Meta:
        model = Apartment
        fields = ('id', 'floor', 'number', 'resident', 'created_at', 'updated_at',)


class PackageRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Package
        fields = ('id', 'retrieved', 'received', 'resident', 'retrieved_check', 'created_at', 'updated_at',)


class PackageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Package
        fields = ('id', 'resident', 'retrieved_check', 'created_at', 'updated_at',)