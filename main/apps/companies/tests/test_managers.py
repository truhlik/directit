from django.test import TestCase

from model_bakery import baker

from ..models import Company
from .. import constants


class CompanyManagerTestCase(TestCase):

    def setUp(self) -> None:
        super(CompanyManagerTestCase, self).setUp()

    def test_owner_single(self):
        user = baker.make('users.User')
        company1 = baker.make('companies.Company')
        company1.owners.set([user])
        company2 = baker.make('companies.Company')
        qs = Company.objects.owner(user)
        self.assertEqual(1, len(qs))
        self.assertEqual(company1.id, qs[0].id)

    def test_owner_multiple(self):
        u1 = baker.make('users.User')
        u2 = baker.make('users.User')
        u3 = baker.make('users.User')
        c1 = baker.make('companies.Company')
        c1.owners.set([u1, u2])
        c2 = baker.make('companies.Company')
        c2.owners.set([u1, u2])
        c3 = baker.make('companies.Company')
        c3.owners.set([u3])
        qs = Company.objects.owner(u1).order_by('id')
        self.assertEqual(2, len(qs))
        self.assertListEqual([c1.id, c2.id], sorted(qs.values_list('id', flat=True)))

    def test_clients(self):
        c1 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CLIENT)
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CONSULTANT)
        c3 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER)

        qs = Company.objects.clients()
        self.assertEqual(1, len(qs))
        self.assertEqual(c1.id, qs[0].id)

    def test_consultants(self):
        c1 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CLIENT)
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CONSULTANT)
        c3 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER)

        qs = Company.objects.consultants()
        self.assertEqual(1, len(qs))
        self.assertEqual(c2.id, qs[0].id)

    def test_suppliers(self):
        c1 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CLIENT)
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CONSULTANT)
        c3 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER)

        qs = Company.objects.suppliers()
        self.assertEqual(1, len(qs))
        self.assertEqual(c3.id, qs[0].id)

    def test_full_text_search(self):
        c1 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='příliš žluťoučký kůň', name_public='příliš žluťoučký kůň')

        qs = Company.objects.full_text_search('kůň')
        self.assertEqual(1, len(qs))
        self.assertEqual(c1.id, qs[0].id)

    def test_consultants_or_suppliers(self):
        c1 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CLIENT)
        c2 = baker.make('companies.Company', role=constants.COMPANY_ROLE_CONSULTANT, name='a')
        c3 = baker.make('companies.Company', role=constants.COMPANY_ROLE_SUPPLIER, name='b')
        qs = Company.objects.consultants_or_suppliers()
        self.assertEqual(2, len(qs))
        self.assertEqual([c2.id, c3.id], list(qs.values_list('id', flat=True)))
