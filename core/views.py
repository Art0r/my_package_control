from core.models import Resident
from core.serializers import ResidentSerializer
from rest_framework import permissions, viewsets


class ResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all().order_by('apto')
    serializer_class = ResidentSerializer
    permission_classes = (permissions.AllowAny,)