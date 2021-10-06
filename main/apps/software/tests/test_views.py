from django.urls import reverse

from model_bakery import baker
from rest_framework.test import APITestCase

from main.apps.companies import constants as company_consts

from ..models import Software


class SoftwareViewsTestCase(APITestCase):

    def setUp(self) -> None:
        super(SoftwareViewsTestCase, self).setUp()
        self.user = baker.make('users.User')
        self.user = baker.make('users.User')
        c = baker.make('companies.Company', role=company_consts.COMPANY_ROLE_CLIENT, plan=company_consts.PROFILE_PREMIUM)
        c.owners.set([self.user])

    def do_auth(self):
        self.client.force_authenticate(user=self.user)

    def test_software_list(self):
        """ Otestuju, že Software endpointy vrací všechny user objekty. """

        s1 = baker.make('software.Software', owner=self.user)
        s2 = baker.make('software.Software')
        s3 = baker.make('software.Software', owner=self.user)
        self.do_auth()
        r = self.client.get(reverse('software-list'))
        self.assertEqual(200, r.status_code)
        self.assertEqual(2, len(r.data['results']))

    def test_software_patch_unauthorized(self):
        """ Otestuju, že Software lze upravovat jen kde je user owner, jinak se vrací 404. """

        s1 = baker.make('software.Software')
        self.do_auth()
        r = self.client.patch(reverse('software-detail', args=(s1.id, )), {'name': 'test'})
        self.assertEqual(404, r.status_code)

    def test_software_patch_authorized(self):
        """ Otestuju, že Software lze upravovat jen kde je user owner. """

        s2 = baker.make('software.Software', owner=self.user)
        self.do_auth()
        r = self.client.patch(reverse('software-detail', args=(s2.id, )), {'name': 'new name'})
        self.assertEqual(200, r.status_code)
        s2.refresh_from_db()
        self.assertEqual('new name', s2.name)

    def test_software_create(self):
        """ Otestuju, že Software lze vytvořit. """

        c1 = baker.make('categories.Category')
        self.do_auth()
        r = self.client.post(reverse('software-list'), {'categories': [c1.id], 'name': 'test', 'licence_count': 1})
        self.assertEqual(201, r.status_code)
        self.assertEqual(1, Software.objects.all().count())
        s = Software.objects.first()
        self.assertEqual(self.user.id, s.owner.id)

    def test_software_delete(self):
        """ Otestuju, že Software lze smazat. """

        s2 = baker.make('software.Software', owner=self.user)
        self.do_auth()
        r = self.client.delete(reverse('software-detail', args=(s2.id,)))
        self.assertEqual(204, r.status_code)
        self.assertEqual(0, Software.objects.all().count())

    def test_software_delete_unathorized(self):
        """ Otestuju, že Software nelze smazat pro nepřihlášené uživatele. """

        s2 = baker.make('software.Software', owner=self.user)
        r = self.client.delete(reverse('software-detail', args=(s2.id,)))
        self.assertEqual(401, r.status_code)

    def test_create_category(self):
        """ Otestuju, že Softwaru lze přidata kategorii. """
        cat = baker.make('categories.Category')
        s2 = baker.make('software.Software', owner=self.user)
        self.do_auth()
        r = self.client.post(reverse('software-categories', args=(s2.id,)), {'id': cat.id})
        self.assertEqual(200, r.status_code)
        self.assertEqual(1, s2.categories.all().count())

    def test_delete_category(self):
        """ Otestuju, že Softwaru lze odebrat kategorie. """

        cat = baker.make('categories.Category')
        s2 = baker.make('software.Software', owner=self.user)
        s2.categories.add(cat)
        self.do_auth()
        r = self.client.delete(reverse('software-categories', args=(s2.id,)), {'id': cat.id})
        self.assertEqual(200, r.status_code)
        self.assertEqual(0, s2.categories.all().count())
