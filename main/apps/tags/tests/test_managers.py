from django.test import TestCase

from model_bakery import baker

from ..models import Tag


class TagManagerTestCase(TestCase):

    def setUp(self) -> None:
        super(TagManagerTestCase, self).setUp()

    def test_full_text_search(self):
        c1 = baker.make('tags.Tag', name='přilíš žluťoučký kůň')
        c2 = baker.make('tags.Tag', name='přilíš červenoučký kůň')
        qs = Tag.objects.full_text_search('zlut')
        self.assertEqual(1, len(qs))
        self.assertEqual(c1.id, qs[0].id)
