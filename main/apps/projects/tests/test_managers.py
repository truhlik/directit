from django.test import TestCase

from model_bakery import baker

from ..models import Project


class ProjectsManagerTestCase(TestCase):

    def setUp(self) -> None:
        super(ProjectsManagerTestCase, self).setUp()

    def test_owner(self):
        user = baker.make('users.User')
        t1 = baker.make('projects.Project', owner=user)
        t2 = baker.make('projects.Project')

        qs = Project.objects.owner(user)
        self.assertEqual(1, len(qs))
        self.assertEqual(t1.id, qs[0].id)

    def test_has_view_perm(self):
        company = baker.make('companies.Company')
        user = baker.make('users.User')
        company.owners.set([user])
        t1 = baker.make('projects.Project', owner=user)
        t2 = baker.make('projects.Project')
        t3 = baker.make('projects.Project', consultant=user.company)
        t4 = baker.make('projects.Project', supplier=user.company)

        qs = Project.objects.has_view_perm(user).order_by('id')
        self.assertEqual(3, len(qs))
        self.assertEqual([t1.id, t3.id, t4.id], [qs[0].id, qs[1].id, qs[2].id])
