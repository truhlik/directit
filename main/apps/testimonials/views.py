from rest_framework import viewsets, permissions
from . import models, serializers


class TestimonialViewSet(viewsets.ModelViewSet):
    """
    Viewsets pro Testimonial.
    """

    queryset = models.Testimonial.objects.prefetch_related('owner', 'company')
    serializer_class = serializers.TestimonialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.action in ['list', 'retrieve']:
            # při čtení mohu zobrazit všechno
            return self.queryset.authorized()
        else:
            # při put, patch, delete vracím jen ty, kde je daný user vlastníkem
            return self.queryset.owner(self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
