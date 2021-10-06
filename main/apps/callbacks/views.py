from rest_framework import viewsets, permissions, mixins
from . import models, serializers
from main.libraries import permissions as perms


class CallbackViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    """
    Viewsets pro Callback se týká vždy objektů patřících danému uživateli,
    takže je dovoleno provádět update, delete apod.
    """

    queryset = models.CallBackRequest.objects.all().callback().prefetch_related('tags')
    serializer_class = serializers.CallBackSerializer
    permission_classes = [permissions.IsAuthenticated & perms.IsClient & perms.HasPaidPlanOrReadOnly]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return models.CallBackRequest.objects.none()
        return super(CallbackViewSet, self).get_queryset().owner(self.request.user)

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save()


class ConsiergeViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    """
    Viewsets pro IT Consierge se týká vždy objektů patřících danému uživateli,
    takže je dovoleno provádět update, delete apod.
    """

    queryset = models.CallBackRequest.objects.all().consierge().prefetch_related('tags')
    serializer_class = serializers.ConsiergeSerializer
    permission_classes = [permissions.IsAuthenticated & perms.HasPaidPlanOrReadOnly]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return models.CallBackRequest.objects.none()
        return super(ConsiergeViewSet, self).get_queryset().owner(self.request.user)

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save()


class ITAssistantViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    """
    Viewsets pro IT Consierge se týká vždy objektů patřících danému uživateli,
    takže je dovoleno provádět update, delete apod.
    """

    queryset = models.CallBackRequest.objects.all().prefetch_related('categories')
    serializer_class = serializers.ITAssistantSerializer
    permission_classes = [permissions.IsAuthenticated & perms.HasPaidPlanOrReadOnly]

    def get_queryset(self):
        return super(ITAssistantViewSet, self).get_queryset().owner(self.request.user)

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save()
