from ares_util.validators import czech_company_id_numeric_validator
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from rest_auth.registration.serializers import RegisterSerializer

from main.apps.companies.constants import COMPANY_ROLE_CLIENT, COMPANY_ROLE_CONSULTANT, COMPANY_ROLE_SUPPLIER
from main.apps.companies.models import Company
from .models import User
from ...libraries.utils import parse_first_and_last_name


class UserRegisterSerializer(RegisterSerializer):

    def validate(self, data):
        # default registration serializer, který aktuálně není enabled
        raise serializers.ValidationError('nemůžete se zde registrovat, přejdete na registraci klienta')


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    email = serializers.EmailField(read_only=True)
    phone = PhoneNumberField()
    role = serializers.CharField()
    plan = serializers.CharField()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'role', 'plan']


class ClientUserRegistrationSerializer(RegisterSerializer):
    company_name = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    job = serializers.CharField(required=False)

    def custom_signup(self, request, user):
        user.phone = self.validated_data['phone']
        user.job = self.validated_data.get('job', None)
        user.save()

        company = Company(
            name=self.validated_data['company_name'],
            role=COMPANY_ROLE_CLIENT,
            email=user.email,
            phone=self.validated_data['phone'],
        )
        company.save()
        company.owners.set([user])


class ConsultantRegistrationSerializer(RegisterSerializer):
    full_name = serializers.CharField()
    phone = serializers.CharField(required=True, max_length=32)
    reg_number = serializers.CharField(required=False, allow_blank=True, allow_null=True, validators=[czech_company_id_numeric_validator])

    def custom_signup(self, request, user):
        user.phone = self.validated_data['phone']
        user.save()

        company = Company(
            name=user.full_name,
            role=COMPANY_ROLE_CONSULTANT,
            email=user.email,
            phone=self.validated_data['phone'],
            reg_number=self.validated_data.get('reg_number'),
        )
        company.save()
        company.owners.set([user])

    def get_cleaned_data(self):
        cleaned_data = super(ConsultantRegistrationSerializer, self).get_cleaned_data()
        full_name = self.validated_data['full_name']
        cleaned_data.update({
            'first_name': parse_first_and_last_name(full_name)[0],
            'last_name': parse_first_and_last_name(full_name)[1]
        })
        return cleaned_data


class SupplierRegistrationSerializer(RegisterSerializer):
    company_name = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    reg_number = serializers.CharField(required=True, validators=[czech_company_id_numeric_validator])

    def custom_signup(self, request, user):
        user.phone = self.validated_data['phone']
        user.save()

        company = Company(
            name=self.validated_data['company_name'],
            role=COMPANY_ROLE_SUPPLIER,
            email=user.email,
            phone=self.validated_data['phone'],
            reg_number=self.validated_data['reg_number'],
        )
        company.save()
        company.owners.set([user])

