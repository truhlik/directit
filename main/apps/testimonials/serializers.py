from rest_framework import serializers

from .models import Testimonial


class TestimonialSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    owner_name = serializers.CharField(source='owner.full_name', read_only=True)
    rating = serializers.IntegerField(required=True)

    class Meta:
        model = Testimonial
        fields = ['id', 'owner_name', 'company', 'rating', 'text']
