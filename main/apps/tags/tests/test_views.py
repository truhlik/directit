from django.urls import reverse

from model_bakery import baker
from rest_framework.test import APITestCase


class TagViewsTestCase(APITestCase):

    def setUp(self) -> None:
        super(TagViewsTestCase, self).setUp()

    def test_tag_list(self):
        """ Otestuju, že Tag endpointy vrací všechny tagy. """

        c1 = baker.make('tags.Tag', name='přilíš žluťoučký kůň')
        c2 = baker.make('tags.Tag', name='přilíš červenoučký kůň')
        r = self.client.get(reverse('tag-list'))
        self.assertEqual(200, r.status_code)
        self.assertEqual(2, len(r.data['results']))

    def test_tag_list_search(self):
        """ Otestuju, že Tag endpointy vrací všechny tagy odpovídající filtru. """

        c1 = baker.make('tags.Tag', name='přilíš žluťoučký kůň')
        c2 = baker.make('tags.Tag', name='nepříliš červenoučký kůň')
        r = self.client.get(reverse('tag-list'), {'q': 'prilís'})
        self.assertEqual(200, r.status_code)
        self.assertEqual(1, len(r.data['results']))
        self.assertEqual(c1.id, r.data['results'][0]['id'])
