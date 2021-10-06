from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from main.libraries import permissions as perms
from main.apps.categories.models import Category
from main.apps.software.serializers import WriteSoftwareSerialier
from . import models, serializers


class SoftwareViewSet(viewsets.ModelViewSet):
    """
    Viewsets pro Software se týká vždy objektů patřících danému uživateli,
    takže je dovoleno provádět update, delete apod.
    """

    queryset = models.Software.objects.all()\
        .prefetch_related('categories', 'owner')
    serializer_class = serializers.SoftwareSerialier
    permission_classes = [permissions.IsAuthenticated & perms.IsClient]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return models.Software.objects.none()
        return super(SoftwareViewSet, self).get_queryset().owner(self.request.user).order_by('licence_till')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update', 'create']:
            return WriteSoftwareSerialier
        return super(SoftwareViewSet, self).get_serializer_class()

    @action(methods=['post', 'delete'], detail=True)
    def categories(self, request, *args, **kwargs):
        obj = self.get_object()
        tag = get_object_or_404(Category, pk=request.data['id'])
        if request.method == 'POST':
            obj.categories.add(tag)
        else:  # delete HTTP metoda
            obj.categories.remove(tag)
        return JsonResponse(data=self.get_serializer(obj, context=self.get_serializer_context()).data)
