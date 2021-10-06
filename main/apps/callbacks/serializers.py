from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

from .models import CallBackRequest
from . import constants


class CallBackSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    phone = PhoneNumberField(required=True)
    time = serializers.TimeField(required=False, allow_null=True)

    class Meta:
        model = CallBackRequest
        fields = ['id', 'name', 'phone', 'time', 'note', 'tags']


class ConsiergeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    phone = PhoneNumberField(required=True)
    time = serializers.TimeField(required=False, allow_null=True)
    callback_type = serializers.ChoiceField(choices=constants.CALLBACK_TYPE_CHOICES, required=True)

    class Meta:
        model = CallBackRequest
        fields = ['id', 'callback_type', 'name', 'phone', 'time', 'note', 'tags']


class ITAssistantSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    phone = PhoneNumberField(required=True)
    time = serializers.TimeField(required=False, allow_null=True)
    assistant_type = serializers.ChoiceField(choices=constants.CALLBACK_TYPE_CHOICES, source='callback_type',
                                             required=False, allow_null=True, allow_blank=True)

    class Meta:
        model = CallBackRequest
        fields = ['id', 'assistant_type', 'name', 'phone', 'time', 'note', 'categories']
