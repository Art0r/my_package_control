from core.serializers.apartment import ApartmentToCondoSerializer
from core.models import Condo
from rest_framework import serializers


class CondoSerializer(serializers.HyperlinkedModelSerializer):
    apto = ApartmentToCondoSerializer(many=True, read_only=True)

    class Meta:
        model = Condo
        fields = ('id', 'street', 'number', 'apto', 'created_at', 'updated_at')
