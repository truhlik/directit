from django.test import TestCase

from model_bakery import baker

from ..serializers import TestimonialSerializer


class TestimonialSerializersTestCase(TestCase):

    def setUp(self) -> None:
        super(TestimonialSerializersTestCase, self).setUp()

    def test_testimonial_serializer_keys(self):
        t = baker.make('testimonials.Testimonial')
        self.assertSetEqual(set(['id', 'owner_name', 'company', 'rating', 'text']),
                            set(TestimonialSerializer(t).data.keys()))
