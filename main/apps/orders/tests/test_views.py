import datetime

from django.urls import reverse

from model_bakery import baker
from rest_framework.test import APITestCase

from main.apps.companies import constants as company_consts
from ..models import Order
from .. import constants


class OrderViewsTestCase(APITestCase):

    def setUp(self) -> None:
        super(OrderViewsTestCase, self).setUp()
        self.user = baker.make('users.User')
        c = baker.make('companies.Company', role=company_consts.COMPANY_ROLE_CLIENT, plan=company_consts.PROFILE_PREMIUM)
        c.owners.set([self.user])

    def do_auth(self):
        self.client.force_authenticate(user=self.user)

    def test_create_for_client_fail(self):
        """ Otestuju, že Order nelze vytvořit na klienta. """

        c1 = baker.make('companies.Company', role=company_consts.COMPANY_ROLE_CLIENT)

        self.do_auth()
        r = self.client.post(reverse('order-list'), data={
            "company": c1.id,
            "note": "",
        }
        )
        self.assertEqual(400, r.status_code)
        self.assertEqual(0, Order.objects.all().count())

    def test_create_with_related_company(self):
        """ Otestuju, že Order lze vytvořit. """

        c1 = baker.make('companies.Company', role=company_consts.COMPANY_ROLE_CONSULTANT)

        self.do_auth()
        r = self.client.post(reverse('order-list'), data={
            "company": c1.id,
            "note": "",
            "duration_unit": constants.MONTH,
            "duration_length": 1,
            "date_from": "2019-01-01"
        }
        )
        self.assertEqual(201, r.status_code)
        self.assertEqual(1, Order.objects.all().count())
        o = Order.objects.all().first()
        self.assertEqual(c1, o.company)
        self.assertEqual(720, o.duration)
        self.assertEqual(datetime.date(2019, 1, 1), o.date_from)

    def test_create_without_related_company(self):
        """ Otestuju, že Order lze vytvořit. """
        t1 = baker.make('products.Product', name='endevel')
        self.do_auth()
        r = self.client.post(reverse('order-list'), data={
            "note": "",
            "products": [t1.id],
        }
        )
        self.assertEqual(201, r.status_code)
        self.assertEqual(1, Order.objects.all().count())
        self.assertEqual(None, Order.objects.all().first().company)

    def test_delete(self):
        """ Otestuju, že Order lze smazat. """

        self.do_auth()
        c1 = baker.make('orders.Order', owner=self.user)
        r = self.client.delete(reverse('order-detail', args=(c1.id, )))
        self.assertEqual(204, r.status_code)
        self.assertEqual(0, Order.objects.all().count())

    def test_delete_unauthorized(self):
        """ Otestuju, že Order nelze smazat, pokud nepatří danému uživateli. """

        self.do_auth()
        c1 = baker.make('orders.Order')
        r = self.client.delete(reverse('order-detail', args=(c1.id, )))
        self.assertEqual(404, r.status_code)
