from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Service
from . import serializers


class ServiceViewSet(ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = serializers.ServiceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
