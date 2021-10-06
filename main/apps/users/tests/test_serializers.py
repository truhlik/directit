from django.test import TestCase

from model_bakery import baker

from ..serializers import UserSerializer, ConsultantRegistrationSerializer
from ...companies.constants import COMPANY_ROLE_SUPPLIER
from rest_framework.test import APIRequestFactory


class UserSerializersTestCase(TestCase):

    def setUp(self) -> None:
        super(UserSerializersTestCase, self).setUp()

    def test_user_serializer_role_value(self):
        c = baker.make('companies.Company', role=COMPANY_ROLE_SUPPLIER)
        u = baker.make('users.User')
        c.owners.set([u])
        serializer = UserSerializer(u)
        self.assertEqual(COMPANY_ROLE_SUPPLIER, serializer.data['role'])

    def test_user_serializer_keys(self):
        c1 = baker.make('users.User')
        self.assertEqual(set(['id', 'first_name', 'last_name', 'email', 'phone', 'role', 'plan']), set(UserSerializer(c1).data.keys()))


class ConsultantRegistrationSerializerTestCase(TestCase):

    def test_valid(self):
        data = {
            "full_name": "cau test",
            "phone": "test",
            "reg_number": "07328958",
            "email": "test@tess.cz",
            "password1": "Ahoj8754",
            "password2": "Ahoj8754",
        }
        serializer = ConsultantRegistrationSerializer(data=data)
        self.assertTrue(serializer.is_valid(raise_exception=True))

    def test_valid_phone(self):
        data = {
            "email": "daniel.vodnansky+konzultant@gmail.com",
            "full_name": "Daniel Vodňanský",
            "password1": "daniel.vodnansky+konzultant@gmail.com",
            "password2": "daniel.vodnansky+konzultant@gmail.com",
            "phone": "daniel.vodnansky+konzultant@gmail.com",
            "reg_number": "06278922",
        }
        serializer = ConsultantRegistrationSerializer(data=data)
        self.assertFalse(serializer.is_valid(raise_exception=False))
        self.assertEqual(1, len(serializer.errors))
        self.assertIn('phone', serializer.errors.keys())

    def test_valid_without_reg_number(self):
        data = {
            "email": "daniel.vodnansky+konzultant@gmail.com",
            "full_name": "Daniel Vodňanský",
            "password1": "daniel.vodnansky+konzultant@gmail.com",
            "password2": "daniel.vodnansky+konzultant@gmail.com",
            "phone": "+420777000112",
            #"reg_number": None,
        }
        serializer = ConsultantRegistrationSerializer(data=data)
        self.assertTrue(serializer.is_valid(raise_exception=True))
