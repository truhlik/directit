from django.urls import reverse

from model_bakery import baker
from rest_framework.test import APITestCase


class CategoriesViewsTestCase(APITestCase):

    def setUp(self) -> None:
        super(CategoriesViewsTestCase, self).setUp()

    def test_categories_list(self):
        """ Otestuju, že Tag endpointy vrací všechny tagy. """

        c1 = baker.make('categories.Category', name='přilíš žluťoučký kůň')
        c2 = baker.make('categories.Category', name='přilíš červenoučký kůň')
        r = self.client.get(reverse('category-list'))
        self.assertEqual(200, r.status_code)
        self.assertEqual(2, len(r.data['results']))

    def test_categories_list_search(self):
        """ Otestuju, že Tag endpointy vrací všechny tagy odpovídající filtru. """

        c1 = baker.make('categories.Category', name='přilíš žluťoučký kůň')
        c2 = baker.make('categories.Category', name='nepřilíš červenoučký kůň')
        r = self.client.get(reverse('category-list'), {'q': 'zlutoucky'})
        self.assertEqual(200, r.status_code)
        self.assertEqual(1, len(r.data['results']))
        self.assertEqual(c1.id, r.data['results'][0]['id'])
