import json

from django.urls import reverse
from model_bakery import baker
from rest_framework.test import APITestCase

from main.apps.companies import constants as company_consts
from main.apps.reference.models import Reference


class ReferenceViewSetTestCase(APITestCase):
    def setUp(self):
        super(ReferenceViewSetTestCase, self).setUp()
        self.user = baker.make('users.User')
        c = baker.make('companies.Company', role=company_consts.COMPANY_ROLE_CLIENT, plan=company_consts.PROFILE_PREMIUM)
        c.owners.set([self.user])

    def do_auth(self):
        self.client.force_authenticate(user=self.user)

    def test_create(self):
        u1 = baker.make('users.User', email='test@test.com')
        self.do_auth()
        r = self.client.post(reverse('reference-list'), data={'owner': u1.id, 'title': 'test', 'sector': 1})

        self.assertEqual(r.status_code, 201)
        self.assertEqual(len(Reference.objects.all()), 1)

    def test_first_letter_name(self):
        r = baker.make('reference.Reference', contact_name='Stepan Cervenka', contact_email='test@test.com')
        self.do_auth()
        r = self.client.get(reverse('reference-detail', args=[r.id, ]))

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data['contact_name'][0], 'S')
        # check if the rest of the string is the same character -> *
        self.assertEqual(all(x == '*' for x in r.data['contact_name'][1:]), True)

        self.assertEqual(r.data['contact_email'][0], 't')
        self.assertEqual(all(x == '*' for x in r.data['contact_email'][1:]), True)

    def test_suggestions(self):
        c = baker.make('categories.Category', name='category')
        p = baker.make('products.Product', name='product')

        ref = baker.make('reference.Reference', category=c, products=[p], title='title')
        self.do_auth()
        r = self.client.get(reverse('reference-suggestion'), data={'q': 'cate'})
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.content)
        self.assertEqual(len(data['results']), 1)
        r = self.client.get(reverse('reference-suggestion'), data={'q': 'pro'})
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.content)
        self.assertEqual(len(data['results']), 1)
        self.assertEqual(data['results'][0], 'product')
        r = self.client.get(reverse('reference-suggestion'), data={'q': 'title'})
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.content)
        self.assertEqual(len(data['results']), 1)

    def test_reference_categories_update(self):
        self.do_auth()
        c1 = baker.make('categories.Category')
        c2 = baker.make('categories.Category')
        ref = baker.make('reference.Reference', category=c1, owner=self.user)
        r = self.client.post(reverse('reference-categories', args=[ref.id]), data={'id': c2.id})
        self.assertEqual(r.status_code, 200)
        ref.refresh_from_db()
        self.assertEqual(ref.category.id, c2.id)
