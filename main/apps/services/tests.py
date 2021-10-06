from django.urls import reverse
from django.test import TestCase
from model_bakery import baker
from rest_framework.test import APITestCase

from main.apps.services.serializers import ServiceSerializer


class ServiceViewSetTestCase(APITestCase):
    def setUp(self):
        super(ServiceViewSetTestCase, self).setUp()
        self.user = baker.make('users.User')
        c = baker.make('companies.Company')
        c.owners.set([self.user])

    def do_auth(self):
        self.client.force_authenticate(user=self.user)

    def test_create_not_allowed(self):
        data = {
            'name': 'test',
            'description': 'test test test test',
            'milestone': 1,
            'category': 1
        }
        r = self.client.post(reverse('service-list'), data=data)
        self.assertEqual(r.status_code, 405)

    def test_detail(self):
        data = {
            'name': 'test',
            'description': 'test test test test',
            'milestone': 1,
        }
        s = baker.make('services.Service', **data)
        self.do_auth()
        r = self.client.get(reverse('service-detail', args=[s.id]))

        for key, value in data.items():
            self.assertEqual(r.data[key], value)


class ServiceSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.serializer_class = ServiceSerializer

    def test_validation(self):
        data = {
            'id': 1,
            'name': 'test',
            'price': 100,
            'description': 'test test test test',
            'milestone': 1,
            'category': 'ANALYZE'
        }
        serializer = self.serializer_class(data=data)

        self.assertEqual(serializer.is_valid(), True)

    def test_validation_without_name_fail(self):
        data = {
            'id': 1,
            'price': 100,
            'description': 'test test test test',
            'milestone': 1,
        }
        serializer = self.serializer_class(data=data)

        self.assertEqual(serializer.is_valid(), False)
