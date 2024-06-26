from typing import Dict, Any

from core.models import Resident, Apartment, Package
from rest_framework import serializers
from core.utils import get_package_hash


class ResidentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Resident
        fields = ('id', 'name', 'email', 'apto', 'phone', 'package', 'created_at', 'updated_at',)


class ApartmentSerializer(serializers.HyperlinkedModelSerializer):
    resident = ResidentSerializer(many=True, read_only=True)

    class Meta:
        model = Apartment
        fields = ('id', 'floor', 'number', 'resident', 'created_at', 'updated_at',)


class PackageRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Package
        fields = ('id', 'retrieved', 'received', 'resident', 'retrieved_check', 'created_at', 'updated_at',)


class PackageUpdateSerializer(serializers.HyperlinkedModelSerializer):
    resident_name = serializers.CharField(max_length=128, write_only=True)
    resident_email = serializers.EmailField(max_length=50, write_only=True)
    resident_apto = serializers.IntegerField(max_value=10000, write_only=True)
    resident_phone = serializers.CharField(max_length=11, write_only=True)

    class Meta:
        model = Package
        fields = ('id', 'updated_at', 'resident_email', 'resident_name', 'resident_apto', 'resident_phone')

    def update(self, instance: Package, validated_data: Dict[str, Any]):
        resident_name = validated_data["resident_name"]
        resident_apto = validated_data["resident_apto"]
        resident_phone = validated_data["resident_phone"]
        resident_email = validated_data["resident_email"]

        retrieved_hash = get_package_hash(
            resident_name=resident_name,
            resident_email=resident_email,
            resident_apto=resident_apto,
            resident_phone=resident_phone
        )

        if instance.received == retrieved_hash:
            instance.retrieved = retrieved_hash
            instance.save()

        return instance


class PackageCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Package
        fields = ('id', 'resident', 'created_at', 'updated_at',)

    def create(self, validated_data: Dict[str, Any]):
        resident = validated_data["resident"]
        package = Package(
            resident=resident,
            received=get_package_hash(
                resident_name=resident.name,
                resident_email=resident.email,
                resident_apto=resident.apto.number,
                resident_phone=resident.phone
            )
        )
        resident.save()
        package.save()
        return resident


class ValidatePackageSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=128, write_only=True)
    name = serializers.CharField(max_length=128, write_only=True)
    apto = serializers.IntegerField(write_only=True)

    class Meta:
        fields = ('email', 'name', 'apto', 'phone')


