from django.urls import reverse

from model_bakery import baker
from rest_framework.test import APITestCase

from main.apps.companies import constants as company_constants

from ..models import CallBackRequest
from .. import constants


class TagViewsTestCase(APITestCase):

    def setUp(self) -> None:
        super(TagViewsTestCase, self).setUp()

    def do_auth(self):
        self.user = baker.make('users.User')
        c = baker.make('companies.Company', role=company_constants.COMPANY_ROLE_CLIENT, plan=company_constants.PROFILE_PREMIUM)
        c.owners.set([self.user])
        self.client.force_authenticate(user=self.user)

    def test_callback_create(self):
        """ Otestuju, že Callback lze vytvořit včetně tagů. """

        self.do_auth()
        t1 = baker.make('tags.Tag')
        t2 = baker.make('tags.Tag')
        r = self.client.post(reverse('callbackrequest-list'), data={
            "callback_type": constants.CALLBACK_TYPE_OTHER,
            "name": "Luboš Truhlář v 10",
            "phone": "777000112",
            "time": "",
            "note": "",
            "tags": [t1.id, t2.id]
        }
        )
        self.assertEqual(201, r.status_code)
        qs = CallBackRequest.objects.all()
        self.assertEqual(1, len(qs))
        obj = qs[0]
        self.assertEqual(2, obj.tags.all().count())
        self.assertEqual(None, obj.callback_type)

    def test_callback_delete(self):
        """ Otestuju, že Callback lze smazat. """

        self.do_auth()
        c1 = baker.make('callbacks.CallBackRequest', user=self.user)
        r = self.client.delete(reverse('callbackrequest-detail', args=(c1.id, )))
        self.assertEqual(204, r.status_code)
        self.assertEqual(0, CallBackRequest.objects.all().count())

    def test_callback_delete_unauthorized(self):
        """ Otestuju, že Callback nelze smazat, pokud nepatří danému uživateli. """

        self.do_auth()
        c1 = baker.make('callbacks.CallBackRequest')
        r = self.client.delete(reverse('callbackrequest-detail', args=(c1.id, )))
        self.assertEqual(404, r.status_code)

    def test_consierge_create(self):
        """ Otestuju, že Callback lze vytvořit včetně tagů. """

        self.do_auth()
        t1 = baker.make('tags.Tag')
        t2 = baker.make('tags.Tag')
        r = self.client.post(reverse('consierge-list'), data={
            "callback_type": constants.CALLBACK_TYPE_OTHER,
            "name": "Luboš Truhlář v 10",
            "phone": "777000112",
            "time": "",
            "note": "",
            "tags": [t1.id, t2.id]
        }
        )
        self.assertEqual(201, r.status_code)
        qs = CallBackRequest.objects.all()
        self.assertEqual(1, len(qs))
        obj = qs[0]
        self.assertEqual(2, obj.tags.all().count())
        self.assertEqual(constants.CALLBACK_TYPE_OTHER, obj.callback_type)

    def test_consierge_delete(self):
        """ Otestuju, že Callback lze smazat. """

        self.do_auth()
        c1 = baker.make('callbacks.CallBackRequest', user=self.user, callback_type=constants.CALLBACK_TYPE_OTHER)
        r = self.client.delete(reverse('consierge-detail', args=(c1.id, )))
        self.assertEqual(204, r.status_code)
        self.assertEqual(0, CallBackRequest.objects.all().count())

    def test_consierge_delete_unauthorized(self):
        """ Otestuju, že Callback nelze smazat, pokud nepatří danému uživateli. """

        self.do_auth()
        c1 = baker.make('callbacks.CallBackRequest', callback_type=constants.CALLBACK_TYPE_OTHER)
        r = self.client.delete(reverse('consierge-detail', args=(c1.id, )))
        self.assertEqual(404, r.status_code)


class TagViewsTestCaseWithBasicPlan(APITestCase):

    def setUp(self) -> None:
        super(TagViewsTestCaseWithBasicPlan, self).setUp()

    def do_auth(self):
        self.user = baker.make('users.User')
        c = baker.make('companies.Company', plan=company_constants.PROFILE_FREE)
        c.owners.set([self.user])
        self.client.force_authenticate(user=self.user)

    def test_callback_create(self):
        """ Otestuju, že Callback lze vytvořit včetně tagů. """

        self.do_auth()
        t1 = baker.make('tags.Tag')
        t2 = baker.make('tags.Tag')
        r = self.client.post(reverse('callbackrequest-list'), data={
            "callback_type": constants.CALLBACK_TYPE_OTHER,
            "name": "Luboš Truhlář v 10",
            "phone": "777000112",
            "time": "",
            "note": "",
            "tags": [t1.id, t2.id]
        }
        )
        self.assertEqual(403, r.status_code)

    def test_callback_delete(self):
        """ Otestuju, že Callback lze smazat. """

        self.do_auth()
        c1 = baker.make('callbacks.CallBackRequest', user=self.user)
        r = self.client.delete(reverse('callbackrequest-detail', args=(c1.id, )))
        self.assertEqual(403, r.status_code)

    def test_callback_delete_unauthorized(self):
        """ Otestuju, že Callback nelze smazat, pokud nepatří danému uživateli. """

        self.do_auth()
        c1 = baker.make('callbacks.CallBackRequest')
        r = self.client.delete(reverse('callbackrequest-detail', args=(c1.id, )))
        self.assertEqual(403, r.status_code)

    def test_consierge_create(self):
        """ Otestuju, že Callback lze vytvořit včetně tagů. """

        self.do_auth()
        t1 = baker.make('tags.Tag')
        t2 = baker.make('tags.Tag')
        r = self.client.post(reverse('consierge-list'), data={
            "callback_type": constants.CALLBACK_TYPE_OTHER,
            "name": "Luboš Truhlář v 10",
            "phone": "777000112",
            "time": "",
            "note": "",
            "tags": [t1.id, t2.id]
        }
        )
        self.assertEqual(403, r.status_code)

    def test_consierge_delete(self):
        """ Otestuju, že Callback lze smazat. """

        self.do_auth()
        c1 = baker.make('callbacks.CallBackRequest', user=self.user, callback_type=constants.CALLBACK_TYPE_OTHER)
        r = self.client.delete(reverse('consierge-detail', args=(c1.id, )))
        self.assertEqual(403, r.status_code)

    def test_consierge_delete_unauthorized(self):
        """ Otestuju, že Callback nelze smazat, pokud nepatří danému uživateli. """

        self.do_auth()
        c1 = baker.make('callbacks.CallBackRequest', callback_type=constants.CALLBACK_TYPE_OTHER)
        r = self.client.delete(reverse('consierge-detail', args=(c1.id, )))
        self.assertEqual(403, r.status_code)
