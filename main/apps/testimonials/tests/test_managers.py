from django.test import TestCase

from model_bakery import baker

from ..models import Testimonial


class TestimonialManagerTestCase(TestCase):

    def setUp(self) -> None:
        super(TestimonialManagerTestCase, self).setUp()

    def test_owner(self):
        user = baker.make('users.User')
        t1 = baker.make('testimonials.Testimonial', owner=user)
        t2 = baker.make('testimonials.Testimonial')

        qs = Testimonial.objects.owner(user)
        self.assertEqual(1, len(qs))
        self.assertEqual(t1.id, qs[0].id)

    def test_authorized(self):
        t1 = baker.make('testimonials.Testimonial')
        t2 = baker.make('testimonials.Testimonial', authorized=True)

        qs = Testimonial.objects.authorized()
        self.assertEqual(1, len(qs))
        self.assertEqual(t2.id, qs[0].id)
