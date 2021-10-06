from django.test import TestCase
from django.utils import timezone

from model_bakery import baker

from ..models import CallBackRequest
from .. import constants


class CompanyManagerTestCase(TestCase):

    def setUp(self) -> None:
        super(CompanyManagerTestCase, self).setUp()

    def test_owner(self):
        user = baker.make('users.User')
        c1 = baker.make('callbacks.CallBackRequest', user=user)
        c2 = baker.make('callbacks.CallBackRequest')
        qs = CallBackRequest.objects.owner(user)
        self.assertEqual(1, len(qs))
        self.assertEqual(c1.id, qs[0].id)

    def test_for_notification_new(self):
        c1 = baker.make('callbacks.CallBackRequest')
        c2 = baker.make('callbacks.CallBackRequest', data={'notification_sent_on': str(timezone.now())})
        qs = CallBackRequest.objects.for_notification()
        self.assertEqual(1, len(qs))
        self.assertEqual(c1.id, qs[0].id)

    def test_for_notification_emtpy_already_notified(self):
        c1 = baker.make('callbacks.CallBackRequest')
        CallBackRequest.objects.all().mark_as_notified()
        c1.refresh_from_db()
        self.assertTrue('notification_sent_on' in c1.data.keys())

