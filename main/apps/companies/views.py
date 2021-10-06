from django.http import JsonResponse, Http404
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404

from main.libraries.functions import get_absolute_url
from main.apps.tags.models import Tag
from main.apps.categories.models import Category
from . import forms, models, serializers
from .serializers import GpsSerializer
from main.libraries.filters import UnAccentSearchFilter
from main.libraries import permissions as perms


class CompanyViewSet(viewsets.ModelViewSet):
    """
    Viewsets pro Company se týká vždy objektů patřících danému uživateli,
    takže je dovoleno provádět update, delete apod.
    """

    queryset = models.Company.objects.all().prefetch_list()
    serializer_class = serializers.CompanyReadSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [UnAccentSearchFilter]
    search_fields = ['name_public', 'tags__name', 'categories__name']

    def get_queryset(self):
        return super(CompanyViewSet, self).get_queryset().owner(self.request.user)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return serializers.WriteCompanySerializer
        return super(CompanyViewSet, self).get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(owners=[self.request.user])

    @action(methods=['post'], detail=True)
    def image(self, request, *args, **kwargs):
        obj = self.get_object()
        form = forms.ImageCompanyForm(self.request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return JsonResponse(data={'image': get_absolute_url(obj.image.url)})
        return JsonResponse(data={'image': ""}, status=400)

    @action(methods=['post', 'delete'], detail=True)
    def tags(self, request, *args, **kwargs):
        obj = self.get_object()
        tag = get_object_or_404(Tag, pk=request.data['id'])
        if request.method == 'POST':
            obj.tags.add(tag)
        else:
            obj.tags.remove(tag)
        return JsonResponse(data=self.get_serializer(obj, context=self.get_serializer_context()).data)

    @action(methods=['post', 'delete'], detail=True)
    def categories(self, request, *args, **kwargs):
        obj = self.get_object()
        tag = get_object_or_404(Category, pk=request.data['id'])
        if request.method == 'POST':
            obj.categories.add(tag)
        else:
            obj.categories.remove(tag)
        return JsonResponse(data=self.get_serializer(obj, context=self.get_serializer_context()).data)

    @action(methods=['get', 'update', 'partial_update'], detail=False)
    def primary(self, request, *args, **kwargs):
        primary_company = self.get_queryset().first()
        if primary_company is None:
            raise Http404

        self.kwargs.update({'pk': primary_company.id})
        if request.method == 'GET':
            return self.retrieve(request, *args, **kwargs)
        elif request.method == 'PUT':
            return self.update(request, *args, **kwargs)
        elif request.method == 'PATCH':
            return self.partial_update(request, *args, **kwargs)
        else:
            raise NotImplementedError()


class SupplierViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Company.objects.suppliers().prefetch_list()
    serializer_class = serializers.CompanyReadSerializer
    filter_backends = [UnAccentSearchFilter]
    search_fields = ['name_public', 'd_tags', 'd_categories']
    permission_classes = [permissions.IsAuthenticated & perms.IsClient]

    def get_serializer_class(self):
        names = ['gps_lng', 'gps_lat', 'name_public']
        query_fields = self.request.query_params.get('fields', '').split(',')
        if all([item in names for item in query_fields]):
            return GpsSerializer
        return super(SupplierViewSet, self).get_serializer_class()

    @action(methods=['get'], detail=False)
    def suggestion(self, request, *args, **kwargs):
        term = request.query_params.get('q', None)
        if not term or len(term) < 3:
            return JsonResponse(data={'results': None})

        results = list(self.get_queryset().full_text_search(term).values_list('name_public', flat=True).distinct())
        results += list(Tag.objects.full_text_search(term).values_list('name', flat=True).distinct())
        results += list(Category.objects.full_text_search(term).values_list('name', flat=True).distinct())
        return JsonResponse(data={'results': results})


class ConsultantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Company.objects.consultants().prefetch_list()
    serializer_class = serializers.UniversalFullCompanySerializer
    filter_backends = [UnAccentSearchFilter]
    search_fields = ['name_public', 'd_tags', 'd_categories']
    permission_classes = [permissions.IsAuthenticated & perms.IsClient & perms.HasPaidPlan]

    def get_serializer_class(self):
        names = ['gps_lng', 'gps_lat', 'name']
        query_fields = self.request.query_params.get('fields', '').split(',')
        if all([item in names for item in query_fields]):
            return GpsSerializer
        return super(ConsultantViewSet, self).get_serializer_class()

    @action(methods=['get'], detail=False)
    def suggestion(self, request, *args, **kwargs):
        term = request.query_params.get('q', None)
        if not term or len(term) < 3:
            return JsonResponse(data={'results': None})

        results = list(Tag.objects.full_text_search(term).values_list('name', flat=True).distinct())
        results += list(Category.objects.full_text_search(term).values_list('name', flat=True).distinct())
        return JsonResponse(data={'results': results})
