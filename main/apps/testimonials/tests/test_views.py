from django.urls import reverse

from model_bakery import baker
from rest_framework.test import APITestCase

from main.apps.testimonials.models import Testimonial


class TagViewsTestCase(APITestCase):

    def setUp(self) -> None:
        super(TagViewsTestCase, self).setUp()
        self.user = baker.make('users.User')

    def do_auth(self):
        self.client.force_authenticate(user=self.user)

    def test_testimonial_list(self):
        """ Otestuju, že Testimonial endpointy vrací všechny authorized testimonialy. """

        t1 = baker.make('testimonials.Testimonial')
        t2 = baker.make('testimonials.Testimonial', authorized=True)
        t2 = baker.make('testimonials.Testimonial', authorized=True)
        self.do_auth()
        r = self.client.get(reverse('testimonial-list'))
        self.assertEqual(200, r.status_code)
        self.assertEqual(2, len(r.data['results']))

    def test_testimonial_patch_unauthorized(self):
        """ Otestuju, že Testimonial lze upravovat jen svoje vrací se 404. """

        t1 = baker.make('testimonials.Testimonial')
        self.do_auth()
        r = self.client.patch(reverse('testimonial-detail', args=(t1.id, )), {'rating': 1})
        self.assertEqual(404, r.status_code)

    def test_testimonial_patch_authorized(self):
        """ Otestuju, že Testimonial lze upravovat jen svoje vrací se 404. """

        t2 = baker.make('testimonials.Testimonial', owner=self.user)
        self.do_auth()
        r = self.client.patch(reverse('testimonial-detail', args=(t2.id, )), {'rating': 3})
        self.assertEqual(200, r.status_code)
        t2.refresh_from_db()
        self.assertEqual(3, t2.rating)

    def test_testimonial_post(self):
        """ Otestuju, že Testimonial lze upravovat jen svoje vrací se 404. """
        c1 = baker.make('companies.Company')
        self.do_auth()
        r = self.client.post(reverse('testimonial-list'),
                             {'rating': 3, 'company': c1.id, 'text': 'test'})
        self.assertEqual(201, r.status_code)
        self.assertEqual(1, Testimonial.objects.all().count())

    def test_testimonial_delete(self):
        """ Otestuju, že Testimonial lze upravovat jen svoje vrací se 404. """
        t2 = baker.make('testimonials.Testimonial', owner=self.user)
        self.do_auth()
        r = self.client.delete(reverse('testimonial-detail', args=(t2.id,)))
        self.assertEqual(204, r.status_code)
        self.assertEqual(0, Testimonial.objects.all().count())
