from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from main.libraries import permissions as perms
from main.apps.categories.models import Category

from . import models, serializers
from .data import get_data


class ProjectViewSet(viewsets.ModelViewSet):
    """
    Viewsets pro Project se týká vždy objektů patřících danému uživateli,
    takže je dovoleno provádět update, delete apod.
    """

    queryset = models.Project.objects.all()\
        .select_related('supplier', 'owner', 'consultant')\
        .prefetch_related('categories')
    serializer_class = serializers.ProjectSerialier
    permission_classes = [
        permissions.IsAuthenticated &
        (perms.IsClient | perms.IsConsultantAndReadOnly | perms.IsSupplierAndReadOnly)
    ]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return models.Project.objects.none()
        return super(ProjectViewSet, self).get_queryset().has_view_perm(self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update', 'create']:
            return serializers.WriteProjectSerialier
        return super(ProjectViewSet, self).get_serializer_class()

    @action(methods=['post', 'delete'], detail=True)
    def categories(self, request, *args, **kwargs):
        obj = self.get_object()
        tag = get_object_or_404(Category, pk=request.data['id'])
        if request.method == 'POST':
            obj.categories.add(tag)
        else:  # delete HTTP metoda
            obj.categories.remove(tag)
        return JsonResponse(data=self.get_serializer(obj, context=self.get_serializer_context()).data)

    @action(methods=['get'], detail=False)
    def default(self, request, *args, **kwargs):
        project_id = request.GET.get('project_id', None)
        return JsonResponse(data=get_data(project_id))
