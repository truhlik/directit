from rest_framework import serializers

from .models import File


class FileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=True)

    class Meta:
        model = File
        fields = ['id', 'file', 'title', 'description']

    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_authenticated:
            validated_data['user'] = user
        return super(FileSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.is_authenticated and instance.user is None:
            validated_data['user'] = user
        return super(FileSerializer, self).update(instance, validated_data)
