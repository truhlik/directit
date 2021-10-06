from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category
from .serializers import CategorySerializer, CategoryGroupingSerializer
from main.libraries.filters import UnAccentSearchFilter


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [UnAccentSearchFilter]
    search_fields = ['name']


class CategoryGroupByViewSet(APIView):

    def get_queryset(self):
        return Category.objects.all().main_category_with_prefetch_subcategories_and_projects()

    def get(self, request, *args, **kwargs):
        qs = self.get_queryset()
        return Response(CategoryGroupingSerializer(qs, many=True).data)
