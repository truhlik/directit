from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from .permissions import IsMessageOwner
from .serializers import MessageSerializer
from .models import Message
from ..projects.models import Project


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().select_related('parent')
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated & IsMessageOwner]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['thread__object_id', 'parent']

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Message.objects.none()

        user = self.request.user
        project_id_list = Project.objects.filter(
            models.Q(owner=user) |
            models.Q(supplier__owners=user) |
            models.Q(consultant__owners=user)
        ).values_list('id', flat=True)
        qs = super(MessageViewSet, self).get_queryset().filter(thread__object_id__in=project_id_list)

        # spočítej počet zpráv v odpovědích
        qs = qs.annotate(_replies=models.Count('children__id'))

        if self.request.query_params.get('parent') is None:
            qs = qs.filter(parent__isnull=True)
        return qs.order_by('-created_at')
