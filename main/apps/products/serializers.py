from rest_framework import serializers

from .models import Product
from ..categories.serializers import CategorySerializer
from ..companies.serializers import UniversalSimpleCompanySerializer
from ..tags.serializers import TagSerializer
from ..vendors.serializers import VendorSerializer


class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    categories = CategorySerializer(many=True)
    suppliers = UniversalSimpleCompanySerializer(many=True)
    vendor = VendorSerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'vendor', 'suppliers', 'categories', 'tags']
