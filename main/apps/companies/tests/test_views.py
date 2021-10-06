import json
from collections import OrderedDict

from django.urls import reverse

from model_bakery import baker
from rest_framework.test import APITestCase

from main.apps.companies import constants as company_constants
from main.apps.companies.models import Company
from .. import constants


class CompanyViewsTestCase(APITestCase):

    def setUp(self) -> None:
        super(CompanyViewsTestCase, self).setUp()
        self.user = baker.make('users.User')
        self.company = baker.make('companies.Company', plan=company_constants.PROFILE_PREMIUM, role=company_constants.COMPANY_ROLE_CLIENT)
        self.company.owners.set([self.user])

    def do_auth(self):
        self.client.force_authenticate(user=self.user)

    def test_company_list_only_for_authenticated_failed(self):
        """ Otestuju, že Company endpointy vyžadují přihlášeného uživatele. """

        r = self.client.get(reverse('company-list'))
        self.assertEqual(401, r.status_code)

    def test_company_list_only_for_authenticated_success(self):
        """ Otestuju, že Company endpointy vyžadují přihlášeného uživatele. """

        self.do_auth()
        r = self.client.get(reverse('company-list'))
        self.assertEqual(200, r.status_code)

    def test_companies_create(self):

        data = {
            "role": "CONSULTANT",
            "name": "Luboš Truhlář",
            "description": "",
            "email": "lubos.truhlar@gmail.com",
            "phone": "777000112",
            "web": "",
            "reg_number": "07328958",
            "vat_number": "",
            "street": "U Stadionu",
            "street_number": "1",
            "city": "Kralupy Nad Vltavou",
            "zip": "27801"
        }

        self.do_auth()
        r = self.client.post(reverse('company-list'), data=data)
        self.assertEqual(201, r.status_code)

        # ověřím, že se správně asocioval owner
        company = Company.objects.get(id=r.data['id'])
        self.assertEqual(self.user.id, company.owners.all().get().id)
        self.assertEqual(constants.COMPANY_ROLE_CONSULTANT, company.role)

    def test_company_update(self):
        data = {
            "role": "CONSULTANT",
            "name": "Luboš Truhlář",
            "description": "",
            "email": "lubos.truhlar@gmail.com",
            "phone": "777000112",
            "web": "",
            "reg_number": "07328958",
            "vat_number": "",
            "street": "U Stadionu",
            "street_number": "1",
            "city": "Kralupy Nad Vltavou",
            "zip": "27801"
        }

        self.do_auth()
        r = self.client.post(reverse('company-list'), data=data)
        self.assertEqual(201, r.status_code)

        # ověřím, že se správně asocioval owner
        self.assertEqual(self.user.id, r.data['owners'][0])

    def test_company_patch(self):
        c1 = baker.make('companies.Company', description='')
        c1.owners.set([self.user])
        data = {'description': 'test'}
        self.do_auth()
        r = self.client.patch(reverse('company-detail', args=(c1.id, )), data=data)
        self.assertEqual(200, r.status_code)
        c1.refresh_from_db()
        self.assertEqual('test', c1.description)

    def test_company_patch_role_not_allowed(self):
        c1 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CLIENT)
        c1.owners.set([self.user])
        data = {'role': constants.COMPANY_ROLE_CONSULTANT}
        self.do_auth()
        r = self.client.patch(reverse('company-detail', args=(c1.id, )), data=data)
        self.assertEqual(400, r.status_code)

    def test_company_tag_create(self):
        c1 = baker.make('companies.Company', description='')
        t1 = baker.make('tags.Tag', name='endevel')
        c1.owners.set([self.user])
        data = {'id': t1.id}
        self.do_auth()
        r = self.client.post(reverse('company-tags', args=(c1.id, )), data=data)
        self.assertEqual(200, r.status_code)
        c1.refresh_from_db()
        self.assertEqual(t1, c1.tags.first())

    def test_company_tag_delete(self):
        c1 = baker.make('companies.Company', description='')
        t1 = baker.make('tags.Tag', name='endevel')
        c1.owners.set([self.user])
        c1.tags.set([t1])
        data = {'id': t1.id}
        self.do_auth()
        r = self.client.delete(reverse('company-tags', args=(c1.id, )), data=data)
        self.assertEqual(200, r.status_code)
        c1.refresh_from_db()
        self.assertEqual(0, len(c1.tags.all()))

    def test_company_category_create(self):
        c1 = baker.make('companies.Company', description='')
        t1 = baker.make('categories.Category', name='endevel')
        c1.owners.set([self.user])
        data = {'id': t1.id}
        self.do_auth()
        r = self.client.post(reverse('company-categories', args=(c1.id, )), data=data)
        self.assertEqual(200, r.status_code)
        c1.refresh_from_db()
        self.assertEqual(t1, c1.categories.first())

    def test_company_category_delete(self):
        c1 = baker.make('companies.Company', description='')
        t1 = baker.make('categories.Category', name='endevel')
        c1.owners.set([self.user])
        c1.categories.set([t1])
        data = {'id': t1.id}
        self.do_auth()
        r = self.client.delete(reverse('company-categories', args=(c1.id, )), data=data)
        self.assertEqual(200, r.status_code)
        c1.refresh_from_db()
        self.assertEqual(0, len(c1.tags.all()))

    def test_companies_list_owner(self):
        company2 = baker.make('companies.Company')

        self.do_auth()
        r = self.client.get(reverse('company-list'))
        self.assertEqual(1, r.data['pagination']['count'])
        self.assertEqual(self.company.id, r.data['results'][0]['id'])

    def test_consultant_list(self):
        c1 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CLIENT)
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CONSULTANT)
        c3 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER)

        self.do_auth()
        r = self.client.get(reverse('consultant-list'))
        self.assertEqual(200, r.status_code)
        self.assertEqual(c2.id, r.data['results'][0]['id'])
        self.assertIn('testimonials', r.data['results'][0])
        self.assertIn('categories', r.data['results'][0])
        self.assertIn('tags', r.data['results'][0])

    def test_supplier_list(self):
        c1 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CLIENT)
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CONSULTANT)
        c3 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='a')
        c4 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='b')

        self.do_auth()
        r = self.client.get(reverse('supplier-list'))
        self.assertEqual(200, r.status_code)
        self.assertEqual(2, len(r.data['results']))
        self.assertEqual(c3.id, r.data['results'][0]['id'])
        self.assertIn('testimonials', r.data['results'][0])
        self.assertIn('categories', r.data['results'][0])
        self.assertIn('tags', r.data['results'][0])

    def test_supplier_list_page_size(self):
        c1 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER)
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER)
        c3 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER)

        self.do_auth()
        r = self.client.get(reverse('supplier-list'), {'page_size': 1, 'page': 2})
        self.assertEqual(200, r.status_code)
        e = OrderedDict([('count', 3),
                         ('next', 'http://testserver/api/v1/suppliers/?page=3&page_size=1'),
                         ('previous', 'http://testserver/api/v1/suppliers/?page_size=1'),
                         ('page', 2),
                         ('num_pages', 3),
                         ('page_size', 1)])
        self.assertEqual(e, r.data['pagination'])

    def test_consultant_list_page_size(self):
        c1 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CONSULTANT)
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CONSULTANT)
        c3 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CONSULTANT)

        self.do_auth()
        r = self.client.get(reverse('consultant-list'), {'page_size': 1, 'page': 2})
        self.assertEqual(200, r.status_code)
        e = OrderedDict([('count', 3),
                         ('next', 'http://testserver/api/v1/consultants/?page=3&page_size=1'),
                         ('previous', 'http://testserver/api/v1/consultants/?page_size=1'),
                         ('page', 2),
                         ('num_pages', 3),
                         ('page_size', 1)])
        self.assertEqual(e, r.data['pagination'])

    def test_consultant_suggestion(self):
        c = baker.make('companies.Company', role=constants.COMPANY_ROLE_CONSULTANT, name='test1')
        t = baker.make('tags.Tag', name='test2')
        cat = baker.make('categories.Category', name='test3')

        _ = baker.make('companies.Company', role=constants.COMPANY_ROLE_CONSULTANT, name='loremi psume')
        _ = baker.make('tags.Tag', name='lorem dolor')
        _ = baker.make('categories.Category', name='lorem dolor sit amet')

        self.do_auth()
        r = self.client.get(reverse('consultant-suggestion') + "?q=test")
        self.assertEqual(200, r.status_code)
        dct = json.loads(r.content)
        self.assertEqual(2, len(dct['results']))
        self.assertEqual(['test2', 'test3'], dct['results'])

    def test_supplier_suggestion(self):
        c = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='test1')
        t = baker.make('tags.Tag', name='test2')
        cat = baker.make('categories.Category', name='test3')

        _ = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='loremi psume')
        _ = baker.make('tags.Tag', name='lorem dolor')
        _ = baker.make('categories.Category', name='lorem dolor sit amet')

        self.do_auth()
        r = self.client.get(reverse('supplier-suggestion') + "?q=test")
        self.assertEqual(200, r.status_code)
        dct = json.loads(r.content)
        self.assertEqual(3, len(dct['results']))
        self.assertEqual(['test1', 'test2', 'test3'], dct['results'])

    def test_consultant_search_by_name(self):
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CONSULTANT)
        c = baker.make('companies.Company', role=constants.COMPANY_ROLE_CONSULTANT, name='přiliš žluťoučký kůň')
        t = baker.make('tags.Tag', name='test2 štěpán')
        c.tags.add(t)
        cat = baker.make('categories.Category', name='test3 čežík')
        c.categories.add(cat)

        self.do_auth()
        r = self.client.get(reverse('consultant-list') + "?q=přiliš")
        self.assertEqual(200, r.status_code)
        dct = json.loads(r.content)
        self.assertEqual(1, len(dct['results']))
        self.assertEqual(c.id, dct['results'][0]['id'])

    def test_consultant_search_by_tag(self):
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER)
        c = baker.make('companies.Company', role=constants.COMPANY_ROLE_CONSULTANT, name='přiliš žluťoučký kůň')
        t = baker.make('tags.Tag', name='test2 štěpán')
        c.tags.add(t)
        cat = baker.make('categories.Category', name='test3 čežík')
        c.categories.add(cat)

        self.do_auth()
        r = self.client.get(reverse('consultant-list') + "?q=těp")
        self.assertEqual(200, r.status_code)
        dct = json.loads(r.content)
        self.assertEqual(1, len(dct['results']))
        self.assertEqual(c.id, dct['results'][0]['id'])

    def test_consultant_search_by_category(self):
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER)
        c = baker.make('companies.Company', role=constants.COMPANY_ROLE_CONSULTANT, name='přiliš žluťoučký kůň')
        t = baker.make('tags.Tag', name='test2 štěpán')
        c.tags.add(t)
        cat = baker.make('categories.Category', name='test3 čežík')
        c.categories.add(cat)

        self.do_auth()
        r = self.client.get(reverse('consultant-list') + "?q=čež")
        self.assertEqual(200, r.status_code)
        dct = json.loads(r.content)
        self.assertEqual(1, len(dct['results']))
        self.assertEqual(c.id, dct['results'][0]['id'])

    def test_supplier_search_by_name(self):
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER)
        c = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='přiliš žluťoučký kůň')
        t = baker.make('tags.Tag', name='test2 štěpán')
        c.tags.add(t)
        cat = baker.make('categories.Category', name='test3 čežík')
        c.categories.add(cat)

        self.do_auth()
        r = self.client.get(reverse('supplier-list') + "?q=žluťou")
        self.assertEqual(200, r.status_code)
        dct = json.loads(r.content)
        self.assertEqual(1, len(dct['results']))
        self.assertEqual(c.id, dct['results'][0]['id'])

    def test_supplier_search_by_tag(self):
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='přiliš žluťoučký kůň')
        c = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='přiliš žluťoučký kůň')
        t = baker.make('tags.Tag', name='test2 štěpán')
        c.tags.add(t)
        cat = baker.make('categories.Category', name='test3 čežík')
        c.categories.add(cat)

        self.do_auth()
        r = self.client.get(reverse('supplier-list') + "?q=těp")
        self.assertEqual(200, r.status_code)
        dct = json.loads(r.content)
        self.assertEqual(1, len(dct['results']))
        self.assertEqual(c.id, dct['results'][0]['id'])

    def test_supplier_search_by_category(self):
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER)
        c = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='přiliš žluťoučký kůň')
        t = baker.make('tags.Tag', name='test2 štěpán')
        c.tags.add(t)
        cat = baker.make('categories.Category', name='test3 čežík')
        c.categories.add(cat)

        self.do_auth()
        r = self.client.get(reverse('supplier-list') + "?q=ežík")
        self.assertEqual(200, r.status_code)
        dct = json.loads(r.content)
        self.assertEqual(1, len(dct['results']))
        self.assertEqual(c.id, dct['results'][0]['id'])


class CompanyViewsWithBasicPlanTestCase(APITestCase):

    def setUp(self) -> None:
        super(CompanyViewsWithBasicPlanTestCase, self).setUp()
        self.user = baker.make('users.User')
        self.company = baker.make('companies.Company', plan=company_constants.PROFILE_FREE, role=company_constants.COMPANY_ROLE_CLIENT)
        self.company.owners.set([self.user])

    def do_auth(self):
        self.client.force_authenticate(user=self.user)

    def test_company_list_only_for_authenticated_failed(self):
        """ Otestuju, že Company endpointy vyžadují přihlášeného uživatele. """

        r = self.client.get(reverse('company-list'))
        self.assertEqual(401, r.status_code)

    def test_company_list_only_for_authenticated_success(self):
        """ Otestuju, že Company endpointy vyžadují přihlášeného uživatele. """

        self.do_auth()
        r = self.client.get(reverse('company-list'))
        self.assertEqual(200, r.status_code)

    def test_companies_create(self):

        data = {
            "role": "CONSULTANT",
            "name": "Luboš Truhlář",
            "description": "",
            "email": "lubos.truhlar@gmail.com",
            "phone": "777000112",
            "web": "",
            "reg_number": "07328958",
            "vat_number": "",
            "street": "U Stadionu",
            "street_number": "1",
            "city": "Kralupy Nad Vltavou",
            "zip": "27801"
        }

        self.do_auth()
        r = self.client.post(reverse('company-list'), data=data)
        self.assertEqual(201, r.status_code)

        # ověřím, že se správně asocioval owner
        company = Company.objects.get(id=r.data['id'])
        self.assertEqual(self.user.id, company.owners.all().get().id)
        self.assertEqual(constants.COMPANY_ROLE_CONSULTANT, company.role)

    def test_company_update(self):
        data = {
            "role": "CONSULTANT",
            "name": "Luboš Truhlář",
            "description": "",
            "email": "lubos.truhlar@gmail.com",
            "phone": "777000112",
            "web": "",
            "reg_number": "07328958",
            "vat_number": "",
            "street": "U Stadionu",
            "street_number": "1",
            "city": "Kralupy Nad Vltavou",
            "zip": "27801"
        }

        self.do_auth()
        r = self.client.post(reverse('company-list'), data=data)
        self.assertEqual(201, r.status_code)

        # ověřím, že se správně asocioval owner
        self.assertEqual(self.user.id, r.data['owners'][0])

    def test_company_patch(self):
        c1 = baker.make('companies.Company', description='')
        c1.owners.set([self.user])
        data = {'description': 'test'}
        self.do_auth()
        r = self.client.patch(reverse('company-detail', args=(c1.id, )), data=data)
        self.assertEqual(200, r.status_code)
        c1.refresh_from_db()
        self.assertEqual('test', c1.description)

    def test_company_patch_role_not_allowed(self):
        c1 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CLIENT)
        c1.owners.set([self.user])
        data = {'role': constants.COMPANY_ROLE_CONSULTANT}
        self.do_auth()
        r = self.client.patch(reverse('company-detail', args=(c1.id, )), data=data)
        self.assertEqual(400, r.status_code)

    def test_company_tag_create(self):
        c1 = baker.make('companies.Company', description='')
        t1 = baker.make('tags.Tag', name='endevel')
        c1.owners.set([self.user])
        data = {'id': t1.id}
        self.do_auth()
        r = self.client.post(reverse('company-tags', args=(c1.id, )), data=data)
        self.assertEqual(200, r.status_code)
        c1.refresh_from_db()
        self.assertEqual(t1, c1.tags.first())

    def test_company_tag_delete(self):
        c1 = baker.make('companies.Company', description='')
        t1 = baker.make('tags.Tag', name='endevel')
        c1.owners.set([self.user])
        c1.tags.set([t1])
        data = {'id': t1.id}
        self.do_auth()
        r = self.client.delete(reverse('company-tags', args=(c1.id, )), data=data)
        self.assertEqual(200, r.status_code)
        c1.refresh_from_db()
        self.assertEqual(0, len(c1.tags.all()))

    def test_company_category_create(self):
        c1 = baker.make('companies.Company', description='')
        t1 = baker.make('categories.Category', name='endevel')
        c1.owners.set([self.user])
        data = {'id': t1.id}
        self.do_auth()
        r = self.client.post(reverse('company-categories', args=(c1.id, )), data=data)
        self.assertEqual(200, r.status_code)
        c1.refresh_from_db()
        self.assertEqual(t1, c1.categories.first())

    def test_company_category_delete(self):
        c1 = baker.make('companies.Company', description='')
        t1 = baker.make('categories.Category', name='endevel')
        c1.owners.set([self.user])
        c1.categories.set([t1])
        data = {'id': t1.id}
        self.do_auth()
        r = self.client.delete(reverse('company-categories', args=(c1.id, )), data=data)
        self.assertEqual(200, r.status_code)
        c1.refresh_from_db()
        self.assertEqual(0, len(c1.tags.all()))

    def test_companies_list_owner(self):
        company2 = baker.make('companies.Company')

        self.do_auth()
        r = self.client.get(reverse('company-list'))
        self.assertEqual(1, r.data['pagination']['count'])
        self.assertEqual(self.company.id, r.data['results'][0]['id'])

    def test_consultant_list(self):
        c1 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CLIENT)
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CONSULTANT)
        c3 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER)

        self.do_auth()
        r = self.client.get(reverse('consultant-list'))
        self.assertEqual(403, r.status_code)

    def test_supplier_list(self):
        c1 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CLIENT)
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CONSULTANT)
        c3 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='a')
        c4 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='b')

        self.do_auth()
        r = self.client.get(reverse('supplier-list'))
        self.assertEqual(200, r.status_code)
        self.assertEqual(2, len(r.data['results']))
        self.assertEqual(c3.id, r.data['results'][0]['id'])
        self.assertIn('testimonials', r.data['results'][0])
        self.assertIn('categories', r.data['results'][0])
        self.assertIn('tags', r.data['results'][0])

    def test_supplier_list_page_size(self):
        c1 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER)
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER)
        c3 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER)

        self.do_auth()
        r = self.client.get(reverse('supplier-list'), {'page_size': 1, 'page': 2})
        self.assertEqual(200, r.status_code)
        e = OrderedDict([('count', 3),
                         ('next', 'http://testserver/api/v1/suppliers/?page=3&page_size=1'),
                         ('previous', 'http://testserver/api/v1/suppliers/?page_size=1'),
                         ('page', 2),
                         ('num_pages', 3),
                         ('page_size', 1)])
        self.assertEqual(e, r.data['pagination'])

    def test_consultant_list_page_size(self):
        c1 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CONSULTANT)
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CONSULTANT)
        c3 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CONSULTANT)

        self.do_auth()
        r = self.client.get(reverse('consultant-list'), {'page_size': 1, 'page': 2})
        self.assertEqual(403, r.status_code)

    def test_consultant_suggestion(self):
        c = baker.make('companies.Company', role=constants.COMPANY_ROLE_CONSULTANT, name='test1')
        t = baker.make('tags.Tag', name='test2')
        cat = baker.make('categories.Category', name='test3')

        _ = baker.make('companies.Company', role=constants.COMPANY_ROLE_CONSULTANT, name='loremi psume')
        _ = baker.make('tags.Tag', name='lorem dolor')
        _ = baker.make('categories.Category', name='lorem dolor sit amet')

        self.do_auth()
        r = self.client.get(reverse('consultant-suggestion') + "?q=test")
        self.assertEqual(403, r.status_code)

    def test_supplier_suggestion(self):
        c = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='test1')
        t = baker.make('tags.Tag', name='test2')
        cat = baker.make('categories.Category', name='test3')

        _ = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='loremi psume')
        _ = baker.make('tags.Tag', name='lorem dolor')
        _ = baker.make('categories.Category', name='lorem dolor sit amet')

        self.do_auth()
        r = self.client.get(reverse('supplier-suggestion') + "?q=test")
        self.assertEqual(200, r.status_code)
        dct = json.loads(r.content)
        self.assertEqual(3, len(dct['results']))
        self.assertEqual(['test1', 'test2', 'test3'], dct['results'])

    def test_supplier_search_by_name(self):
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER)
        c = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='přiliš žluťoučký kůň')
        t = baker.make('tags.Tag', name='test2 štěpán')
        c.tags.add(t)
        cat = baker.make('categories.Category', name='test3 čežík')
        c.categories.add(cat)

        self.do_auth()
        r = self.client.get(reverse('supplier-list') + "?q=žluťou")
        self.assertEqual(200, r.status_code)
        dct = json.loads(r.content)
        self.assertEqual(1, len(dct['results']))
        self.assertEqual(c.id, dct['results'][0]['id'])

    def test_supplier_search_by_tag(self):
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER)
        c = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='přiliš žluťoučký kůň')
        t = baker.make('tags.Tag', name='test2 štěpán')
        c.tags.add(t)
        cat = baker.make('categories.Category', name='test3 čežík')
        c.categories.add(cat)

        self.do_auth()
        r = self.client.get(reverse('supplier-list') + "?q=těp")
        self.assertEqual(200, r.status_code)
        dct = json.loads(r.content)
        self.assertEqual(1, len(dct['results']))
        self.assertEqual(c.id, dct['results'][0]['id'])

    def test_supplier_search_by_category(self):
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER)
        c = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='přiliš žluťoučký kůň')
        t = baker.make('tags.Tag', name='test2 štěpán')
        c.tags.add(t)
        cat = baker.make('categories.Category', name='test3 čežík')
        c.categories.add(cat)

        self.do_auth()
        r = self.client.get(reverse('supplier-list') + "?q=ežík")
        self.assertEqual(200, r.status_code)
        dct = json.loads(r.content)
        self.assertEqual(1, len(dct['results']))
        self.assertEqual(c.id, dct['results'][0]['id'])

    def test_supplier_search_by_multiple_categories(self):
        c3 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='kolobrnda')
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='kolobrnda')
        c1 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='kolobrnda')
        cat1 = baker.make('categories.Category', name='jedna')
        cat2 = baker.make('categories.Category', name='dva')
        c1.categories.set([cat1, cat2])
        c2.categories.set([cat1])
        tag1 = baker.make('tags.Tag', name='django')
        tag2 = baker.make('tags.Tag', name='office')
        c1.tags.set([tag1, tag2])
        c2.tags.set([tag1])

        self.do_auth()
        r = self.client.get(reverse('supplier-list') + "?q=dva,jedna")
        self.assertEqual(200, r.status_code)
        dct = json.loads(r.content)
        self.assertEqual(1, len(dct['results']))
        self.assertEqual(c1.id, dct['results'][0]['id'])

    def test_supplier_search_by_multiple_tags(self):
        c3 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='kolobrnda')
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='kolobrnda')
        c1 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='kolobrnda')
        cat1 = baker.make('categories.Category', name='jedna')
        cat2 = baker.make('categories.Category', name='dva')
        c1.categories.set([cat1, cat2])
        c2.categories.set([cat1])
        tag1 = baker.make('tags.Tag', name='django')
        tag2 = baker.make('tags.Tag', name='office')
        c1.tags.set([tag1, tag2])
        c2.tags.set([tag1])

        self.do_auth()
        r = self.client.get(reverse('supplier-list') + "?q=django,office")
        self.assertEqual(200, r.status_code)
        dct = json.loads(r.content)
        self.assertEqual(1, len(dct['results']))
        self.assertEqual(c1.id, dct['results'][0]['id'])

    def test_supplier_search_by_multiple_category_and_tag(self):
        c3 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='kolobrnda')
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='kolobrnda')
        c1 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='kolobrnda')
        cat1 = baker.make('categories.Category', name='jedna')
        cat2 = baker.make('categories.Category', name='dva')
        c1.categories.set([cat1, cat2])
        c2.categories.set([cat1])
        tag1 = baker.make('tags.Tag', name='django')
        tag2 = baker.make('tags.Tag', name='office')
        c1.tags.set([tag1, tag2])
        c2.tags.set([tag1])

        self.do_auth()
        r = self.client.get(reverse('supplier-list') + "?q=office,dva")
        self.assertEqual(200, r.status_code)
        dct = json.loads(r.content)
        self.assertEqual(1, len(dct['results']))
        self.assertEqual(c1.id, dct['results'][0]['id'])

    def test_supplier_search_by_multiple_category_and_name(self):
        c3 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='kolobrnda')
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='kolobrnda')
        c1 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='kolobrnda')
        cat1 = baker.make('categories.Category', name='jedna')
        cat2 = baker.make('categories.Category', name='dva')
        c1.categories.set([cat1, cat2])
        c2.categories.set([cat1])
        tag1 = baker.make('tags.Tag', name='django')
        tag2 = baker.make('tags.Tag', name='office')
        c1.tags.set([tag1, tag2])
        c2.tags.set([tag1])

        self.do_auth()
        r = self.client.get(reverse('supplier-list') + "?q=dva,kolobrnda")
        self.assertEqual(200, r.status_code)
        dct = json.loads(r.content)
        self.assertEqual(1, len(dct['results']))
        self.assertEqual(c1.id, dct['results'][0]['id'])

    def test_supplier_search_by_multiple_tag_and_name(self):
        c3 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='kolobrnda')
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='kolobrnda')
        c1 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='kolobrnda')
        cat1 = baker.make('categories.Category', name='jedna')
        cat2 = baker.make('categories.Category', name='dva')
        cat3 = baker.make('categories.Category', name='tri')
        c1.categories.set([cat1, cat2, cat3])
        c2.categories.set([cat1, cat2])
        c3.categories.set([cat3])
        tag1 = baker.make('tags.Tag', name='django')
        tag2 = baker.make('tags.Tag', name='office')
        tag3 = baker.make('tags.Tag', name='smtp')
        tag4 = baker.make('tags.Tag', name='ansible')
        c1.tags.set([tag1, tag2, tag3])
        c2.tags.set([tag1, tag2])
        c3.tags.set([tag1, tag4])

        self.do_auth()
        r = self.client.get(reverse('supplier-list') + "?q=smtp,kolobrnda")
        self.assertEqual(200, r.status_code)
        dct = json.loads(r.content)
        self.assertEqual(1, len(dct['results']))
        self.assertEqual(c1.id, dct['results'][0]['id'])

    def test_supplier_list_gps_only(self):
        c1 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CLIENT)
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CONSULTANT)
        c3 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='a')
        c4 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='b')

        self.do_auth()
        r = self.client.get(reverse('supplier-list') + '?fields=gps_lng,gps_lat,name')
        self.assertEqual(200, r.status_code)
