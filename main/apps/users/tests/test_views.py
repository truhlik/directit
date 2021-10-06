from allauth.account.models import EmailAddress
from django.test import Client
from django.urls import reverse

from model_bakery import baker
from rest_framework.test import APITestCase

from main.apps.companies.constants import COMPANY_ROLE_CLIENT, COMPANY_ROLE_CONSULTANT, COMPANY_ROLE_SUPPLIER
from main.apps.users.models import User


class UserSerializersTestCase(APITestCase):

    def setUp(self) -> None:
        super(UserSerializersTestCase, self).setUp()

    def do_auth(self):
        self.client.force_authenticate(user=self.user)

    def test_register_view(self):
        client = Client()

        url_reg = reverse('rest_register')
        resp = client.post(url_reg, {'email': 'test@test.cz', 'password1': 'test1324', 'password2': 'test1324'},
                           content_type='application/json')

        # simple registration is not allowed, use client or consultant registration
        self.assertEqual(400, resp.status_code)

    def test_login_view(self):
        client = Client()
        # user = baker.make('users.User', email='test@test.cz', is_active=True)
        # user.set_password('test1324')

        # nevím proč nefunguje manuální vytvoření uživatele viz. výše (možná nějaké cache, confirmace apod.)

        data = {
            'company_name': 'Test',
            'phone': '777000111',
            'email': 'test@test.cz',
            'password1': 'test1324',
            'password2': 'test1324'
        }

        url_reg = reverse('registration-client')
        client.post(url_reg, data, content_type='application/json')

        EmailAddress.objects.filter(user=User.objects.first()).update(verified=True)
        url = reverse('rest_login')
        resp = client.post(url, {'email': 'test@test.cz', 'password': 'test1324'}, content_type='application/json')
        self.assertEqual(200, resp.status_code)
        self.assertTrue('key' in resp.json())

    def test_self_view_get(self):
        self.user = baker.make('users.User')
        self.do_auth()
        r = self.client.get(reverse('user-self'))
        self.assertEqual(200, r.status_code)
        self.assertEqual(str(self.user.id), r.json()['id'])

    def test_self_view_patch(self):
        self.user = baker.make('users.User', first_name='Luboš', last_name='Truhlář')
        self.do_auth()
        r = self.client.patch(reverse('user-self'), {'first_name': 'test1',
                                                     'last_name': 'test2',
                                                     'phone': '777000112'
                                                     })
        self.assertEqual(200, r.status_code)
        self.assertEqual(
            ['test1', 'test2', '+420777000112'],
            [r.json()['first_name'], r.json()['last_name'], r.json()['phone']]
        )

    def test_register_client_failed_missing_company_data(self):
        client = Client()

        url_reg = reverse('registration-client')
        resp = client.post(url_reg, {'email': 'test@test.cz', 'password1': 'test1324', 'password2': 'test1324'},
                           content_type='application/json')

        self.assertEqual(400, resp.status_code)
        self.assertEqual(2, len(resp.data))
        self.assertTrue('company_name' in resp.data.keys())
        self.assertTrue('phone' in resp.data.keys())

    def test_register_client_success(self):
        client = Client()
        data = {
            'company_name': 'Test',
            'phone': '777000111',
            'email': 'test@test.cz',
            'password1': 'test1324',
            'password2': 'test1324'
        }
        url_reg = reverse('registration-client')
        resp = client.post(url_reg, data,
                           content_type='application/json')

        self.assertEqual(201, resp.status_code)
        u_qs = User.objects.all()
        user = u_qs[0]
        self.assertEqual(1, len(u_qs))
        self.assertTrue(1, len(user.companies.all()))
        self.assertEqual(COMPANY_ROLE_CLIENT, user.companies.all().first().role)

    def test_register_consultant_failed_missing_phone(self):
        client = Client()

        url_reg = reverse('registration-consultant')
        resp = client.post(url_reg, {
            'full_name': 'test',
            'email': 'test@test.cz',
            'password1': 'test1324',
            'password2': 'test1324',
            'reg_number': '07328958'
        },
                           content_type='application/json')

        self.assertEqual(400, resp.status_code)
        self.assertEqual(1, len(resp.data))
        self.assertTrue('phone' in resp.data.keys())

    def test_register_consultant_success(self):
        client = Client()
        data = {
            'full_name': "cau test",
            'phone': '777000111',
            'email': 'test@test.cz',
            'password1': 'test1324',
            'password2': 'test1324',
            'reg_number': '07328958'
        }
        url_reg = reverse('registration-consultant')
        resp = client.post(url_reg, data, content_type='application/json')

        self.assertEqual(201, resp.status_code)
        u_qs = User.objects.all()
        user = u_qs[0]
        self.assertEqual(1, len(u_qs))
        self.assertTrue(1, len(user.companies.all()))
        self.assertEqual(COMPANY_ROLE_CONSULTANT, user.companies.all().first().role)
        self.assertEqual('07328958', user.companies.all().first().reg_number)
        self.assertEqual('cau test', user.companies.all().first().name)

    def test_register_supplier_failed_missing_phone(self):
        client = Client()

        url_reg = reverse('registration-supplier')
        resp = client.post(url_reg, {
            'company_name': 'test',
            'email': 'test@test.cz',
            'password1': 'test1324',
            'password2': 'test1324',
            'reg_number': '07328958'
        },
                           content_type='application/json')

        self.assertEqual(400, resp.status_code)
        self.assertEqual(1, len(resp.data))
        self.assertTrue('phone' in resp.data.keys())

    def test_register_supplier_success(self):
        client = Client()
        data = {
            'company_name': 'test',
            'phone': '777000111',
            'email': 'test@test.cz',
            'password1': 'test1324',
            'password2': 'test1324',
            'reg_number': '07328958'
        }
        url_reg = reverse('registration-supplier')
        resp = client.post(url_reg, data, content_type='application/json')

        self.assertEqual(201, resp.status_code)
        u_qs = User.objects.all()
        user = u_qs[0]
        self.assertEqual(1, len(u_qs))
        self.assertTrue(1, len(user.companies.all()))
        self.assertEqual(COMPANY_ROLE_SUPPLIER, user.companies.all().first().role)
        self.assertEqual('07328958', user.companies.all().first().reg_number)
        self.assertEqual('test', user.companies.all().first().name)
