from core.models import Resident, Apartment, Package
from rest_framework import serializers
from core.utils import get_package_hash


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


class PackageUpdateSerializer(serializers.HyperlinkedModelSerializer):
    resident_name = serializers.CharField(max_length=128, write_only=True)
    resident_email = serializers.EmailField(max_length=50, write_only=True)
    resident_apto = serializers.IntegerField(max_value=2000, write_only=True)

    class Meta:
        model = Package
        fields = ('id', 'updated_at', 'resident_email', 'resident_name', 'resident_apto')


class PackageCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Package
        fields = ('id', 'resident', 'created_at', 'updated_at',)

    def create(self, validated_data):
        resident = validated_data["resident"]
        resident.package.received = get_package_hash(
            resident_name=resident.name,
            resident_email=resident.email,
            resident_apto=resident.apto.number
        )
        return super().create(validated_data)


class ValidatePackageSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=128, write_only=True)
    name = serializers.CharField(max_length=128, write_only=True)
    apto = serializers.IntegerField(write_only=True)

    class Meta:
        fields = ('email', 'name', 'apto')


