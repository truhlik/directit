from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from .models import Reference
from .serializers import ReferenceSerializer, ReferenceWriteSerializer
from main.libraries.filters import UnAccentSearchFilter
from main.apps.categories.models import Category
from main.apps.products.models import Product
from main.libraries.permissions import IsOwnerOrReadOnly


class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()\
        .select_related('owner', 'solver', 'category')\
        .prefetch_related('products')
    serializer_class = ReferenceSerializer
    filter_backends = [UnAccentSearchFilter]
    search_fields = ['title', 'category__name', 'products__name', 'problem_text', 'solution_text', 'benefits_text']
    permission_classes = [permissions.IsAuthenticated & IsOwnerOrReadOnly]

    def get_queryset(self):
        qs = super(ReferenceViewSet, self).get_queryset()
        if self.request.query_params.get('owner') == 'true':
            return qs.filter(owner=self.request.user)
        return qs

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ReferenceWriteSerializer
        return super(ReferenceViewSet, self).get_serializer_class()

    @action(methods=['get'], detail=False)
    def suggestion(self, request, *args, **kwargs):
        term = request.query_params.get('q', None)
        if not term or len(term) < 3:
            return JsonResponse(data={'results': None})

        results = list(self.get_queryset().full_text_search(term).values_list('title', flat=True).distinct())
        results += list(Category.objects.full_text_search(term).values_list('name', flat=True).distinct())
        results += list(Product.objects.full_text_search(term).values_list('name', flat=True).distinct())
        return JsonResponse(data={'results': results})

    @action(methods=['post', 'delete'], detail=True)
    def categories(self, request, *args, **kwargs):
        if request.data.get('id') is None:
            return HttpResponseBadRequest('missing category id in request data')
        obj = self.get_object()
        cat = get_object_or_404(Category, pk=request.data['id'])
        if request.method == 'POST':
            obj.category = cat
        else:  # delete HTTP metoda
            obj.category = None
        obj.save()
        return JsonResponse(data=self.get_serializer(obj, context=self.get_serializer_context()).data)
