from django.test import TestCase

from model_bakery import baker

from ..serializers import TagSerializer


class TagSerializersTestCase(TestCase):

    def setUp(self) -> None:
        super(TagSerializersTestCase, self).setUp()

    def test_tag_serializer_keys(self):
        c1 = baker.make('tags.Tag')
        self.assertSetEqual(set(['id', 'name', 'image', 'categories']),
                            set(TagSerializer(c1).data.keys()))
