from rest_framework import serializers

from .models import Reference
from main.apps.categories.serializers import CategorySerializer
from main.apps.companies.serializers import UniversalFullCompanySerializer
from main.apps.products.serializers import ProductSerializer
from ..files.models import File
from ..files.serializers import FileSerializer


class ReferenceSerializer(serializers.ModelSerializer):
    solver_obj = UniversalFullCompanySerializer(source='solver', read_only=True)
    category_obj = CategorySerializer(source='category', read_only=True)
    products_obj = ProductSerializer(source='products', many=True, read_only=True)
    sector_obj = serializers.SerializerMethodField()
    files = serializers.PrimaryKeyRelatedField(queryset=File.objects.all().select_related('user'), many=True, required=False)
    files_obj = FileSerializer(many=True, required=False, read_only=True, source='files')
    can_edit = serializers.SerializerMethodField(read_only=True)
    contact_email = serializers.CharField(required=False, allow_null=True, allow_blank=True, source='public_contact_email')
    contact_name = serializers.CharField(required=False, allow_null=True, allow_blank=True, source='public_contact_name')

    class Meta:
        model = Reference
        fields = [
            "id",
            "client_name",
            # "solver",
            "solver_obj",
            "category",
            "category_obj",
            "products",
            "products_obj",
            "sector",
            "sector_obj",
            "title",
            "contact_name",
            "contact_email",
            "problem_text",
            "solution_text",
            "benefits_text",
            "files",
            "files_obj",
            "can_edit",
        ]

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        validated_data['solver'] = self.context['request'].user.company
        return super(ReferenceSerializer, self).create(validated_data)

    # def validate_solver(self, company):
    #     if company.role not in [company_constatns.COMPANY_ROLE_CONSULTANT, company_constatns.COMPANY_ROLE_SUPPLIER]:
    #         raise serializers.ValidationError('vámi zvolená společnost má klientskou roli, '
    #                                           'musíte zvolit společnost s rolí dodavatel nebo konzultant')
    #     return company

    def validate_files(self, files):
        for file in files:
            if file.user != self.context['request'].user:
                raise serializers.ValidationError('you are not owner of given file {}'.format(file.id))
        return files

    def get_can_edit(self, obj) -> bool:
        return obj.owner == self.context['request'].user

    def get_sector_obj(self, obj) -> dict:
        return {"id": obj.sector, "name": obj.get_sector_display()}


class ReferenceWriteSerializer(ReferenceSerializer):
    contact_email = serializers.CharField(required=False, allow_null=True, allow_blank=True, )
    contact_name = serializers.CharField(required=False, allow_null=True, allow_blank=True, )
