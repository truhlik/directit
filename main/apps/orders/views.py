from rest_framework import viewsets, permissions, mixins

from main.libraries import permissions as perms

from . import models, serializers


class OrderViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    """
    Viewsets pro OrderCompany se týká vždy objektů patřících danému uživateli,
    takže je dovoleno provádět update, delete apod.
    """

    queryset = models.Order.objects.all().select_related('company').prefetch_related('products', 'categories')
    serializer_class = serializers.OrderSerializer
    permission_classes = [permissions.IsAuthenticated & perms.IsClient & perms.HasPaidPlan]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return models.Order.objects.none()
        return super(OrderViewSet, self).get_queryset().owner(self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
