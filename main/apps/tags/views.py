from rest_framework import viewsets

from .models import Tag
from .serializers import TagSerializer
from main.libraries.filters import UnAccentSearchFilter


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [UnAccentSearchFilter]
    search_fields = ['^name']
