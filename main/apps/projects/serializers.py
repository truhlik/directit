from rest_framework import serializers

from main.apps.categories.models import Category
from main.apps.categories.serializers import CategorySerializer
from .models import Project
from . import constants
from ..companies.serializers import CompanyReadSerializer
from ..files.models import File
from ..files.serializers import FileSerializer
from ...libraries.emails import CustomerEmailProject


class JSONDataField(serializers.BooleanField):

    def __init__(self, *args, **kwargs):
        self.key = kwargs.pop('key')
        super(JSONDataField, self).__init__(*args, **kwargs)

    def to_representation(self, value):
        value = value.get(self.key, None)
        return super(JSONDataField, self).to_representation(value)

    def to_internal_value(self, data):
        return super(JSONDataField, self).to_internal_value(data)


class ProjectSerialier(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    categories = CategorySerializer(many=True, read_only=True)
    status = serializers.ChoiceField(choices=constants.PROJECT_STATUS_CHOICES, default=constants.PROJECT_STATUS_NEW)
    step1 = serializers.ChoiceField(choices=constants.PROJECT_STEP_CHOICES, source='step1int', default=constants.PROJECT_STEP_NOT_DEMAND)
    step2 = serializers.ChoiceField(choices=constants.PROJECT_STEP_CHOICES, source='step2int', default=constants.PROJECT_STEP_NOT_DEMAND)
    step3 = serializers.ChoiceField(choices=constants.PROJECT_STEP_CHOICES, source='step3int', default=constants.PROJECT_STEP_NOT_DEMAND)
    step4 = serializers.ChoiceField(choices=constants.PROJECT_STEP_CHOICES, source='step4int', default=constants.PROJECT_STEP_NOT_DEMAND)
    step5 = serializers.ChoiceField(choices=constants.PROJECT_STEP_CHOICES, source='step5int', default=constants.PROJECT_STEP_NOT_DEMAND)
    step6 = serializers.ChoiceField(choices=constants.PROJECT_STEP_CHOICES, source='step6int', default=constants.PROJECT_STEP_NOT_DEMAND)
    consultant = CompanyReadSerializer(read_only=True)
    supplier = CompanyReadSerializer(read_only=True)
    files = FileSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'categories', 'name', 'description', 'due_date', 'status', 'consultant', 'supplier', 'files',
                  'step1', 'step2', 'step3', 'step4', 'step5', 'step6']


class WriteProjectSerialier(ProjectSerialier):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True, required=False)
    files = serializers.PrimaryKeyRelatedField(queryset=File.objects.all().select_related('user'), many=True, required=False)

    def validate_files(self, files):
        for file in files:
            if file.user != self.context['request'].user:
                raise serializers.ValidationError('you are not owner of given file {}'.format(file.id))
        return files

    def create(self, validated_data):
        instance = super(WriteProjectSerialier, self).create(validated_data)
        CustomerEmailProject(instance).send_html_email(instance.owner.email)
        return instance
