from rest_framework import serializers

from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    pass

    class Meta:
        model = Tag
        fields = '__all__'
