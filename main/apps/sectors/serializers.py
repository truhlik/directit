from rest_framework import serializers


class SectorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
