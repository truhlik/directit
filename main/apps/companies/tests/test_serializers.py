from django.test import TestCase

from model_bakery import baker

from ..serializers import CompanyReadSerializer, WriteCompanySerializer


class CompanySerializersTestCase(TestCase):

    def setUp(self) -> None:
        super(CompanySerializersTestCase, self).setUp()

    def test_company_read_serializer_keys(self):
        c1 = baker.make('companies.Company')
        self.assertSetEqual(set(['id', 'image', 'reg_number', 'tags', 'categories', 'created_at', 'updated_at', 'role',
                                 'plan', 'name', 'description', 'email', 'phone', 'web', 'vat_number', 'street',
                                 'street_number', 'city', 'zip', 'gps_lat', 'gps_lng', 'owners', 'address',
                                 'testimonials']),
                            set(CompanyReadSerializer(c1).data.keys()))

    def test_company_write_serializer_keys(self):
        c1 = baker.make('companies.Company')
        self.assertSetEqual(set(['id', 'image', 'reg_number', 'tags', 'categories', 'created_at', 'updated_at', 'role',
                                 'name', 'description', 'email', 'phone', 'web', 'vat_number', 'street',
                                 'street_number', 'city', 'zip', 'gps_lat', 'gps_lng', 'owners', 'address']),
                            set(WriteCompanySerializer(c1).data.keys()))

    def test_write_serializer_validate_success(self):
        data = {
            "role": "CONSULTANT",
            "name": "Luboš Truhlář",
            "description": "",
            "email": "lubos.truhlar@gmail.com",
            "phone": "777000112",
            "web": "www.endevel.cz",
            "reg_number": "07328958",
            "vat_number": "",
            "street": "U Stadionu",
            "street_number": "1",
            "city": "Kralupy Nad Vltavou",
            "zip": "27801"
        }
        serializer = WriteCompanySerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_write_serializer_validate_without_web(self):
        data = {
            "role": "CONSULTANT",
            "name": "Luboš Truhlář",
            "description": "",
            "email": "lubos.truhlar@gmail.com",
            "phone": "777000112",
            "web": "",
            "reg_number": "07328958",
            "vat_number": "",
            "street": "U Stadionu",
            "street_number": "1",
            "city": "Kralupy Nad Vltavou",
            "zip": "27801"
        }
        serializer = WriteCompanySerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_write_serializer_validate_without_http_prefix(self):
        data = {
            "role": "CONSULTANT",
            "name": "Luboš Truhlář",
            "description": "",
            "email": "lubos.truhlar@gmail.com",
            "phone": "777000112",
            "web": "www.endevel.cz",
            "reg_number": "07328958",
            "vat_number": "",
            "street": "U Stadionu",
            "street_number": "1",
            "city": "Kralupy Nad Vltavou",
            "zip": "27801"
        }
        serializer = WriteCompanySerializer(data=data)
        serializer.is_valid()
        self.assertEqual('http://www.endevel.cz', serializer.validated_data['web'])
