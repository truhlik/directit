from django.test import TestCase

from model_bakery import baker

from ..models import Software


class SoftwareManagerTestCase(TestCase):

    def setUp(self) -> None:
        super(SoftwareManagerTestCase, self).setUp()

    def test_owner(self):
        user = baker.make('users.User')
        t1 = baker.make('software.Software', owner=user)
        t2 = baker.make('software.Software')

        qs = Software.objects.owner(user)
        self.assertEqual(1, len(qs))
        self.assertEqual(t1.id, qs[0].id)
