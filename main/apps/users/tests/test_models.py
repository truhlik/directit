from django.test import TestCase
from django_redis import get_redis_connection

from model_bakery import baker
from main.apps.companies import constants as company_constants
from main.apps.companies.models import UserCompany


class UserSerializersTestCase(TestCase):

    def setUp(self) -> None:
        super(UserSerializersTestCase, self).setUp()

    def test_user_full_name(self):
        u = baker.make('users.User', first_name='Luboš', last_name='Truhlář')
        self.assertEqual('Luboš Truhlář', u.full_name)

    def test_company_without_company(self):
        u = baker.make('users.User')
        self.assertIsNone(u.company)

    def test_company_with_company(self):
        u = baker.make('users.User')
        c = baker.make('companies.Company')
        UserCompany(user=u, company=c).save()
        self.assertEqual(c, u.company)

    def test_has_paid_plan_without_company(self):
        u = baker.make('users.User')
        self.assertFalse(u.has_paid_plan())

    def test_has_paid_plan_free(self):
        u = baker.make('users.User')
        c = baker.make('companies.Company', plan=company_constants.PROFILE_FREE)
        UserCompany(user=u, company=c).save()
        self.assertFalse(u.has_paid_plan())

    def test_has_paid_plan_basic(self):
        u = baker.make('users.User')
        c = baker.make('companies.Company', plan=company_constants.PROFILE_BASIC)
        UserCompany(user=u, company=c).save()
        self.assertTrue(u.has_paid_plan())

    def test_has_paid_plan_premium(self):
        u = baker.make('users.User')
        c = baker.make('companies.Company', plan=company_constants.PROFILE_PREMIUM)
        UserCompany(user=u, company=c).save()
        self.assertTrue(u.has_paid_plan())

    def test_is_client_true(self):
        u = baker.make('users.User')
        c = baker.make('companies.Company', role=company_constants.COMPANY_ROLE_CLIENT)
        UserCompany(user=u, company=c).save()
        self.assertTrue(u.is_client())

    def test_is_client_false(self):
        u = baker.make('users.User')
        c = baker.make('companies.Company', role=company_constants.COMPANY_ROLE_CONSULTANT)
        UserCompany(user=u, company=c).save()
        self.assertFalse(u.is_client())

    def test_is_client_empty(self):
        u = baker.make('users.User')
        self.assertFalse(u.is_client())

    def test_is_consultant_true(self):
        u = baker.make('users.User')
        c = baker.make('companies.Company', role=company_constants.COMPANY_ROLE_CONSULTANT)
        UserCompany(user=u, company=c).save()
        self.assertTrue(u.is_consultant())

    def test_is_consultant_false(self):
        u = baker.make('users.User')
        c = baker.make('companies.Company', role=company_constants.COMPANY_ROLE_CLIENT)
        UserCompany(user=u, company=c).save()
        self.assertFalse(u.is_consultant())

    def test_is_consultant_empty(self):
        u = baker.make('users.User')
        self.assertFalse(u.is_consultant())

    def test_is_supplier_true(self):
        u = baker.make('users.User')
        c = baker.make('companies.Company', role=company_constants.COMPANY_ROLE_SUPPLIER)
        UserCompany(user=u, company=c).save()
        self.assertTrue(u.is_supplier())

    def test_is_supplier_false(self):
        u = baker.make('users.User')
        c = baker.make('companies.Company', role=company_constants.COMPANY_ROLE_CONSULTANT)
        UserCompany(user=u, company=c).save()
        self.assertFalse(u.is_supplier())

    def test_is_supplier_empty(self):
        u = baker.make('users.User')
        self.assertFalse(u.is_supplier())

    def tearDown(self) -> None:
        get_redis_connection("default").flushall()
        return super(UserSerializersTestCase, self).tearDown()
