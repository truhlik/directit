from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    pass

    class Meta:
        model = Category
        fields = ['id', 'name']


class CategoryWithAnnotatedProjects(serializers.ModelSerializer):
    products_count = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']


class CategoryGroupingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    subcategories = CategoryWithAnnotatedProjects(many=True, source='children')

    class Meta:
        model = Category
        fields = ['id', 'name', 'subcategories']

