from django.urls import reverse
from django.utils import timezone

from model_bakery import baker
from rest_framework.test import APITestCase
from main.apps.companies import constants as company_constants
from ..models import Project


class ProjectViewsAsClientTestCase(APITestCase):

    def setUp(self) -> None:
        super(ProjectViewsAsClientTestCase, self).setUp()
        self.user = baker.make('users.User')
        c = baker.make('companies.Company', role=company_constants.COMPANY_ROLE_CLIENT)
        c.owners.set([self.user])

    def do_auth(self):
        self.client.force_authenticate(user=self.user)

    def test_list(self):
        """ Otestuju, že Project endpointy vrací všechny uživatelovi objekty. """

        s1 = baker.make('projects.Project', owner=self.user)
        s2 = baker.make('projects.Project')
        s3 = baker.make('projects.Project', owner=self.user)
        self.do_auth()
        r = self.client.get(reverse('project-list'))
        self.assertEqual(200, r.status_code)
        self.assertEqual(2, len(r.data['results']))

    def test_detail(self):
        """ Otestuju, že Project endpointy vrací všechny uživatelovi objekty. """

        s1 = baker.make('projects.Project', owner=self.user, step1int=10, step6int=0)
        self.do_auth()
        r = self.client.get(reverse('project-detail', args=(s1.id, )))
        self.assertEqual(200, r.status_code)

    def test_patch_unauthorized(self):
        """ Otestuju, že Project lze upravovat jen kde je user owner, jinak se vrací 404. """

        s1 = baker.make('projects.Project')
        self.do_auth()
        r = self.client.patch(reverse('project-detail', args=(s1.id, )), {'name': 'test'})
        self.assertEqual(404, r.status_code)

    def test_patch_authorized(self):
        """ Otestuju, že Project lze upravovat jen kde je user owner. """

        s2 = baker.make('projects.Project', owner=self.user)
        self.do_auth()
        r = self.client.patch(reverse('project-detail', args=(s2.id, )), {'name': 'new name'})
        self.assertEqual(200, r.status_code)
        s2.refresh_from_db()
        self.assertEqual('new name', s2.name)

    def test_create(self):
        """ Otestuju, že Project lze vytvořit. """

        c1 = baker.make('categories.Category')
        self.do_auth()
        r = self.client.post(reverse('project-list'),
                             {'categories': [c1.id],
                              'name': 'test',
                              'description': 'test',
                              'due_date': '2019-01-01',
                              })
        self.assertEqual(201, r.status_code)
        self.assertEqual(1, Project.objects.all().count())
        s = Project.objects.first()
        self.assertEqual(self.user.id, s.owner.id)

    def test_delete(self):
        """ Otestuju, že Project lze smazat. """

        s2 = baker.make('projects.Project', owner=self.user)
        self.do_auth()
        r = self.client.delete(reverse('project-detail', args=(s2.id,)))
        self.assertEqual(204, r.status_code)
        self.assertEqual(0, Project.objects.all().count())

    def test_delete_unathorized(self):
        """ Otestuju, že Project nelze smazat pro nepřihlášené uživatele. """

        s2 = baker.make('projects.Project', owner=self.user)
        r = self.client.delete(reverse('project-detail', args=(s2.id,)))
        self.assertEqual(401, r.status_code)

    def test_create_category(self):
        """ Otestuju, že Project lze přidata kategorii. """
        cat = baker.make('categories.Category')
        s2 = baker.make('projects.Project', owner=self.user)
        self.do_auth()
        r = self.client.post(reverse('project-categories', args=(s2.id,)), {'id': cat.id})
        self.assertEqual(200, r.status_code)
        self.assertEqual(1, s2.categories.all().count())

    def test_delete_category(self):
        """ Otestuju, že Project lze odebrat kategorie. """

        cat = baker.make('categories.Category')
        s2 = baker.make('projects.Project', owner=self.user)
        s2.categories.add(cat)
        self.do_auth()
        r = self.client.delete(reverse('project-categories', args=(s2.id,)), {'id': cat.id})
        self.assertEqual(200, r.status_code)
        self.assertEqual(0, s2.categories.all().count())

    def test_default_endpoint(self):
        self.do_auth()
        r = self.client.get(reverse('project-default'), {'project_id': 2})
        self.assertEqual(200, r.status_code)
        exp_data = {
            'categories': [],
            'name': 'Cloud vs. On-Premise',
            'description': 'Analýza alternativ pro vybraný systém',
            'step1': 10, 'step2': 10, 'step3': 10, 'step4': 0, 'step5': 0, 'step6': 0,
            'due_date': '{}'.format((timezone.now().date() + timezone.timedelta(days=90)).strftime('%Y-%m-%d'))
        }
        self.assertEqual(exp_data, r.json())


class ProjectViewsAsConsultatntTestCase(APITestCase):

    def setUp(self) -> None:
        super(ProjectViewsAsConsultatntTestCase, self).setUp()
        self.user = baker.make('users.User')
        c = baker.make('companies.Company', role=company_constants.COMPANY_ROLE_CONSULTANT)
        c.owners.set([self.user])

    def do_auth(self):
        self.client.force_authenticate(user=self.user)

    def test_list(self):
        """ Otestuju, že Project endpointy vrací všechny uživatelovi objekty. """

        s1 = baker.make('projects.Project', consultant=self.user.company)
        s2 = baker.make('projects.Project')
        s3 = baker.make('projects.Project', consultant=self.user.company)
        self.do_auth()
        r = self.client.get(reverse('project-list'))
        self.assertEqual(200, r.status_code)
        self.assertEqual(2, len(r.data['results']))

    def test_detail(self):
        """ Otestuju, že Project endpointy vrací všechny uživatelovi objekty. """

        s1 = baker.make('projects.Project', consultant=self.user.company, step1int=10, step6int=0)
        self.do_auth()
        r = self.client.get(reverse('project-detail', args=(s1.id, )))
        self.assertEqual(200, r.status_code)

    def test_patch_authorized(self):
        """ Otestuju, že Project lze upravovat jen kde je user owner. """

        s2 = baker.make('projects.Project', consultant=self.user.company)
        self.do_auth()
        r = self.client.patch(reverse('project-detail', args=(s2.id, )), {'name': 'new name'})
        self.assertEqual(403, r.status_code)

    def test_create(self):
        """ Otestuju, že Project lze vytvořit. """

        c1 = baker.make('categories.Category')
        self.do_auth()
        r = self.client.post(reverse('project-list'),
                             {'categories': [c1.id],
                              'name': 'test',
                              'description': 'test',
                              'due_date': '2019-01-01',
                              })
        self.assertEqual(403, r.status_code)

    def test_delete(self):
        """ Otestuju, že Project lze smazat. """

        s2 = baker.make('projects.Project', consultant=self.user.company)
        self.do_auth()
        r = self.client.delete(reverse('project-detail', args=(s2.id,)))
        self.assertEqual(403, r.status_code)

    def test_create_category(self):
        """ Otestuju, že Project lze přidata kategorii. """
        cat = baker.make('categories.Category')
        s2 = baker.make('projects.Project', consultant=self.user.company)
        self.do_auth()
        r = self.client.post(reverse('project-categories', args=(s2.id,)), {'id': cat.id})
        self.assertEqual(403, r.status_code)

    def test_delete_category(self):
        """ Otestuju, že Project lze odebrat kategorie. """

        cat = baker.make('categories.Category')
        s2 = baker.make('projects.Project', consultant=self.user.company)
        s2.categories.add(cat)
        self.do_auth()
        r = self.client.delete(reverse('project-categories', args=(s2.id,)), {'id': cat.id})
        self.assertEqual(403, r.status_code)

    def test_default_endpoint(self):
        self.do_auth()
        r = self.client.get(reverse('project-default'), {'project_id': 2})
        self.assertEqual(200, r.status_code)
        exp_data = {
            'categories': [],
            'name': 'Cloud vs. On-Premise',
            'description': 'Analýza alternativ pro vybraný systém',
            'step1': 10, 'step2': 10, 'step3': 10, 'step4': 0, 'step5': 0, 'step6': 0,
            'due_date': '{}'.format((timezone.now().date() + timezone.timedelta(days=90)).strftime('%Y-%m-%d'))
        }
        self.assertEqual(exp_data, r.json())


class ProjectViewsAsSupplierTestCase(APITestCase):

    def setUp(self) -> None:
        super(ProjectViewsAsSupplierTestCase, self).setUp()
        self.user = baker.make('users.User')
        c = baker.make('companies.Company', role=company_constants.COMPANY_ROLE_SUPPLIER)
        c.owners.set([self.user])

    def do_auth(self):
        self.client.force_authenticate(user=self.user)

    def test_list(self):
        """ Otestuju, že Project endpointy vrací všechny uživatelovi objekty. """

        s1 = baker.make('projects.Project', supplier=self.user.company)
        s2 = baker.make('projects.Project')
        self.do_auth()
        r = self.client.get(reverse('project-list'))
        self.assertEqual(200, r.status_code)
        self.assertEqual(1, len(r.data['results']))
        self.assertEqual(s1.id, r.data['results'][0]['id'])

    def test_detail(self):
        """ Otestuju, že Project endpointy vrací všechny uživatelovi objekty. """

        s1 = baker.make('projects.Project', supplier=self.user.company, step1int=10, step6int=0)
        self.do_auth()
        r = self.client.get(reverse('project-detail', args=(s1.id, )))
        self.assertEqual(200, r.status_code)

    def test_patch_authorized(self):
        """ Otestuju, že Project lze upravovat jen kde je user owner. """

        s2 = baker.make('projects.Project', consultant=self.user.company)
        self.do_auth()
        r = self.client.patch(reverse('project-detail', args=(s2.id, )), {'name': 'new name'})
        self.assertEqual(403, r.status_code)

    def test_create(self):
        """ Otestuju, že Project lze vytvořit. """

        c1 = baker.make('categories.Category')
        self.do_auth()
        r = self.client.post(reverse('project-list'),
                             {'categories': [c1.id],
                              'name': 'test',
                              'description': 'test',
                              'due_date': '2019-01-01',
                              })
        self.assertEqual(403, r.status_code)

    def test_delete(self):
        """ Otestuju, že Project lze smazat. """

        s2 = baker.make('projects.Project', consultant=self.user.company)
        self.do_auth()
        r = self.client.delete(reverse('project-detail', args=(s2.id,)))
        self.assertEqual(403, r.status_code)

    def test_create_category(self):
        """ Otestuju, že Project lze přidata kategorii. """
        cat = baker.make('categories.Category')
        s2 = baker.make('projects.Project', consultant=self.user.company)
        self.do_auth()
        r = self.client.post(reverse('project-categories', args=(s2.id,)), {'id': cat.id})
        self.assertEqual(403, r.status_code)

    def test_delete_category(self):
        """ Otestuju, že Project lze odebrat kategorie. """

        cat = baker.make('categories.Category')
        s2 = baker.make('projects.Project', consultant=self.user.company)
        s2.categories.add(cat)
        self.do_auth()
        r = self.client.delete(reverse('project-categories', args=(s2.id,)), {'id': cat.id})
        self.assertEqual(403, r.status_code)

    def test_default_endpoint(self):
        self.do_auth()
        r = self.client.get(reverse('project-default'), {'project_id': 2})
        self.assertEqual(200, r.status_code)

