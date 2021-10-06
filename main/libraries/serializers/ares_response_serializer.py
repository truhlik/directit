from rest_framework import serializers


class AresResponseSerializer(serializers.Serializer):
    city = serializers.CharField()
    street = serializers.CharField()
    street_number = serializers.CharField()
    zip = serializers.CharField()
    vat_number = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    name = serializers.CharField()
