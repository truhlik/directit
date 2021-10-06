from django.utils.translation import ugettext as _

from rest_framework import serializers

from main.apps.companies.models import Company
from main.apps.orders.utils import get_duration_length
from .models import Order
from . import constants
from ..companies.serializers import UniversalSimpleCompanySerializer
from main.apps.files.serializers import FileSerializer


class OrderSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.consultants_or_suppliers(), required=False)
    rel_name = serializers.SerializerMethodField()
    company_obj = UniversalSimpleCompanySerializer(source='company', read_only=True)
    duration_length = serializers.IntegerField(label='doba trvání', required=False)
    duration_unit = serializers.ChoiceField(label='jednotka', choices=constants.DURATION_UNIT_CHOICES, required=False)
    files = FileSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'company', 'rel_name', 'company_obj', 'date_from', 'duration_length', 'duration_unit', 'note',
                  'products', 'categories', 'files']

    def get_rel_name(self, obj):
        if obj.company is not None:
            return obj.company.name_public

        else:
            product_names = [product.name for product in obj.products.all()]
            cat_names = [cat.name for cat in obj.categories.all()]
            return ", ".join(product_names + cat_names)

    def validate(self, attrs):
        if attrs.get('duration_length', None) and not attrs.get('duration_unit', None):
            raise serializers.ValidationError({'duration_unit': _('musíte vyplnit toto pole')})

        if not attrs.get('duration_length', None) and attrs.get('duration_unit', None):
            raise serializers.ValidationError({'duration_length': _('musíte vyplnit toto pole')})

        # pokud nemám company ani produkty ani kategorie, tak raisni error
        if not attrs.get('company', None) and not attrs.get('products', None) and not attrs.get('categories', None):
            raise serializers.ValidationError({
                'categories': _('musíte zvolit nějakou kategorii nebo produkt'),
                'products': _('musíte zvolit nějakou kategorii nebo produkt'),
            })

        return attrs

    def save(self, **kwargs):
        duration_length = self.validated_data.pop('duration_length', None)
        duration_unit = self.validated_data.pop('duration_unit', None)
        if duration_length and duration_unit:
            kwargs['duration'] = get_duration_length(duration_unit, duration_length)
        return super(OrderSerializer, self).save(**kwargs)
