from core.models import Resident
from rest_framework import serializers


class ResidentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resident
        fields = ('id', 'apto', 'name', 'email',)