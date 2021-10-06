from rest_framework import viewsets, authentication, permissions

from .models import File
from .serializers import FileSerializer


class FilesViewSets(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return File.objects.none()
        return super(FilesViewSets, self).get_queryset().owner(self.request.user)
