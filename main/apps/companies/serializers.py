from rest_framework import serializers

from main.apps.testimonials.serializers import TestimonialSerializer
from main.libraries.serializers.mixins import DynamicFieldsMixin
from .models import Company
from main.apps.tags.serializers import TagSerializer
from main.apps.categories.serializers import CategorySerializer
from .utils import first_letter_name, first_letter_in_word
from ...libraries.functions import get_absolute_url
from django.utils.translation import ugettext as _
from ...libraries.serializers.fields import HyperlinkedSorlImageField  # noqa


class GpsSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True, source='name_public')
    gps_lat = serializers.CharField(read_only=True)
    gps_lng = serializers.CharField(read_only=True)


class BaseCompanySerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    # todo uncomment when sorl-thumbnail==12.6.0 will be released on Pypi
    # image = HyperlinkedSorlImageField('128x128', options={"crop": "center"}, read_only=True)
    id = serializers.IntegerField(read_only=True)
    image = serializers.SerializerMethodField()
    reg_number = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    address = serializers.CharField(read_only=True)
    web = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    class Meta:
        model = Company
        fields = [
            'id', 'image', 'reg_number', 'tags', 'categories', 'created_at', 'updated_at', 'role',
            'plan', 'name', 'description', 'email', 'phone', 'web', 'vat_number', 'street',
            'street_number', 'city', 'zip', 'gps_lat', 'gps_lng', 'owners', 'address',
            'testimonials'
        ]

    def get_image(self, obj):
        if obj.image:
            return get_absolute_url(obj.image.url)
        return ''

    def validate_web(self, attrs):
        if attrs and len(attrs) > 4 and not attrs.startswith('http'):
            return 'http://{}'.format(attrs)
        return attrs


class FirstLetterSerializerField(serializers.CharField):

    def to_representation(self, value):
        value = super(FirstLetterSerializerField, self).to_representation(value).format()
        return first_letter_name(value)


class FirstWordSerializerField(serializers.CharField):

    def to_representation(self, value):
        value = super(FirstWordSerializerField, self).to_representation(value).format()
        return first_letter_in_word(value)


class CompanyReadSerializer(BaseCompanySerializer):
    tags = TagSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    testimonials = TestimonialSerializer(many=True)


class WriteCompanySerializer(BaseCompanySerializer):
    id = serializers.IntegerField(read_only=True)

    def validate_role(self, attr):
        # není možné měnit role firem při update, při create musím umožnit nastavit
        if self.instance is None:
            return attr

        if self.instance.role != attr:
            raise serializers.ValidationError(_('Nemůžete měnit typ firmy.'))

        return attr

    class Meta:
        model = Company
        fields = [
            'id', 'image', 'reg_number', 'tags', 'categories', 'created_at', 'updated_at', 'role',
            'name', 'description', 'email', 'phone', 'web', 'vat_number', 'street',
            'street_number', 'city', 'zip', 'gps_lat', 'gps_lng', 'owners', 'address',
        ]


class UniversalSimpleCompanySerializer(BaseCompanySerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(source='name_public')
    email = serializers.CharField(source='email_public')
    phone = serializers.CharField(source='phone_public')

    class Meta:
        model = Company
        fields = ['id', 'name', 'email', 'phone']


class UniversalFullCompanySerializer(BaseCompanySerializer):
    name = serializers.CharField(source='name_public')
    email = serializers.CharField(source='email_public')
    phone = serializers.CharField(source='phone_public')
    reg_number = serializers.CharField(source='reg_number_public')

    tags = TagSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    testimonials = TestimonialSerializer(many=True)

    class Meta:
        model = Company
        fields = BaseCompanySerializer.Meta.fields
