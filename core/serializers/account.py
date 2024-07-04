from core.models import Account
from rest_framework import serializers
from .condo import CondoSerializer


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    condo = CondoSerializer(many=False, read_only=True)

    class Meta:
        model = Account
        fields = ('id', 'email', 'username',
                  'phone', 'is_staff', 'is_active',
                  'condo', 'created_at', 'updated_at')
