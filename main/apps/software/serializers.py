from rest_framework import serializers

from main.apps.categories.models import Category
from main.apps.categories.serializers import CategorySerializer
from .models import Software


class SoftwareSerialier(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    find_alternative = serializers.BooleanField(required=False, default=False)
    categories = CategorySerializer(many=True)

    class Meta:
        model = Software
        fields = ['id', 'categories', 'name', 'service_contact', 'licence_type', 'licence_unit', 'licence_count',
                  'licence_till', 'find_alternative', 'watch_expiration', 'need_extension', 'need_customization',
                  'need_upgrade']


class WriteSoftwareSerialier(SoftwareSerialier):
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
