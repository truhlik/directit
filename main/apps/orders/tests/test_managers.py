from django.test import TestCase
from django.utils import timezone

from model_bakery import baker

from ..models import Order


class OrderManagerTestCase(TestCase):

    def setUp(self) -> None:
        super(OrderManagerTestCase, self).setUp()

    def test_owner(self):
        user = baker.make('users.User')
        c1 = baker.make('orders.Order', owner=user)
        c2 = baker.make('orders.Order')
        qs = Order.objects.owner(user)
        self.assertEqual(1, len(qs))
        self.assertEqual(c1.id, qs[0].id)

    def test_for_notification_new(self):
        c1 = baker.make('orders.Order')
        c2 = baker.make('orders.Order', data={'notification_sent_on': str(timezone.now())})
        qs = Order.objects.for_notification()
        self.assertEqual(1, len(qs))
        self.assertEqual(c1.id, qs[0].id)

    def test_for_notification_emtpy_already_notified(self):
        c1 = baker.make('orders.Order')
        Order.objects.all().mark_as_notified()
        c1.refresh_from_db()
        self.assertTrue('notification_sent_on' in c1.data.keys())
