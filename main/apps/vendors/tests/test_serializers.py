from django.test import TestCase

from main.apps.vendors.serializers import VendorSerializer


class VendorSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.data = {
            'id': '12',
            'name': 'test'
        }
        self.serializer_class = VendorSerializer

    def test_validation(self):
        serializer = self.serializer_class(data=self.data)
        self.assertEqual(serializer.is_valid(), True)

    def test_validation_without_name_fail(self):
        serializer = self.serializer_class(data=self.data.update(**{'name': None}))
        self.assertEqual(serializer.is_valid(), False)