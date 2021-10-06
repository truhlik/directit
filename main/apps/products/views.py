from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action

from .models import Product
from .serializers import ProductSerializer
from main.libraries.filters import UnAccentSearchFilter
from ..categories.models import Category
from ..tags.models import Tag


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()\
        .prefetch_related('categories', 'tags__categories', 'suppliers')\
        .select_related('vendor')\
        .order_by('name')
    serializer_class = ProductSerializer
    filter_backends = [UnAccentSearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    filterset_fields = ['categories']

    @action(methods=['get'], detail=False)
    def suggestion(self, request, *args, **kwargs):
        term = request.query_params.get('q', None)
        if not term or len(term) < 3:
            return JsonResponse(data={'results': None})

        results = list(Tag.objects.full_text_search(term).values_list('name', flat=True).distinct())
        results += list(Category.objects.full_text_search(term).values_list('name', flat=True).distinct())
        results += list(Product.objects.full_text_search(term).values_list('name', flat=True).distinct())
        return JsonResponse(data={'results': results})
