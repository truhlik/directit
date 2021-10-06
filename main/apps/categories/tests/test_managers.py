from django.test import TestCase

from model_bakery import baker

from ..models import Category


class CategorySerializersTestCase(TestCase):

    def setUp(self) -> None:
        super(CategorySerializersTestCase, self).setUp()

    def test_full_text_search(self):
        c1 = baker.make('categories.Category', name='přilíš žluťoučký kůň')
        c2 = baker.make('categories.Category', name='přilíš červenoučký kůň')
        qs = Category.objects.full_text_search('cerven')
        self.assertEqual(1, len(qs))
        self.assertEqual(c2.id, qs[0].id)

    def test_main_category_with_prefetch_subcategories_and_projects(self):
        c1 = baker.make('categories.Category', parent=None)
        c2 = baker.make('categories.Category', parent=c1)
        qs = Category.objects.main_category_with_prefetch_subcategories_and_projects()
        self.assertEqual(1, len(qs))
        self.assertEqual(c1.id, qs[0].id)