from django.test import TestCase

from model_bakery import baker

from ..serializers import SoftwareSerialier


class SoftwareSerializersTestCase(TestCase):

    def setUp(self) -> None:
        super(SoftwareSerializersTestCase, self).setUp()

    def test_software_serializer_keys(self):
        s = baker.make('software.Software')
        self.assertSetEqual(set(['id', 'categories', 'name', 'service_contact', 'licence_type', 'licence_unit',
                                 'licence_count', 'licence_till', 'find_alternative', 'watch_expiration', 'need_extension',
                                 'need_customization', 'need_upgrade']),
                            set(SoftwareSerialier(s).data.keys()))

    def test_software_serializer_categories_iner(self):
        c = baker.make('categories.Category')
        s = baker.make('software.Software')
        s.categories.add(c)
        self.assertEqual({'id': c.id, 'name': c.name}, SoftwareSerialier(s).data['categories'][0])
