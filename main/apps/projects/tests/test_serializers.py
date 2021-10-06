import json

from django.core import mail
from django.http import HttpRequest
from django.test import TestCase

from model_bakery import baker
from rest_framework.request import Request

from main.apps.projects.models import Project
from ..serializers import ProjectSerialier, WriteProjectSerialier
from .. import constants
from ...companies.constants import COMPANY_ROLE_CONSULTANT


class ProjectSerializersTestCase(TestCase):

    def setUp(self) -> None:
        super(ProjectSerializersTestCase, self).setUp()

    def test_keys(self):
        s = baker.make('projects.Project')
        self.assertSetEqual(
            set(['id', 'categories', 'name', 'description', 'due_date', 'status', 'consultant', 'supplier', 'files',
                 'step1', 'step2', 'step3', 'step4', 'step5', 'step6', ]),
            set(ProjectSerialier(s).data.keys())
        )

    def test_data_steps_fields(self):
        s1 = baker.make('projects.Project', step1int=10, step2int=0, step3int=0, step4int=0, step5int=0, step6int=0)

        data = ProjectSerialier(s1).data
        self.assertEqual(10, data['step1'])
        self.assertEqual(0, data['step2'])

    def test_serializer_categories_inner(self):
        c = baker.make('categories.Category')
        s = baker.make('projects.Project')
        s.categories.add(c)
        self.assertEqual({'id': c.id, 'name': c.name}, ProjectSerialier(s).data['categories'][0])

    def test_assigned_consultant(self):
        c = baker.make('companies.Company', role=COMPANY_ROLE_CONSULTANT)
        p = baker.make('projects.Project', consultant=c)
        serializer = ProjectSerialier(p)
        self.assertEqual(COMPANY_ROLE_CONSULTANT, serializer.data['consultant']['role'])

    def test_save(self):
        with self.settings(CELERY_TASK_ALWAYS_EAGER=True):
            u = baker.make('users.User')
            c = baker.make('categories.Category')
            data = '{"name": "test", "description": "volitelná poznámka", "due_date": "2019-01-01", "status": 10,' \
                   '"step1": 0, "step2": 10, "step3": 0, "step4": 10, "step5": 0, "step6": 10,' \
                   ' "categories": [%s]}' % c.id
            serializer = WriteProjectSerialier(data=json.loads(data))
            serializer.is_valid(raise_exception=True)
            serializer.save(owner=u)
            project = Project.objects.all().first()
            self.assertEqual(u.id, project.owner.id)
            self.assertEqual(c.id, project.categories.all().first().id)
            self.assertEqual(constants.PROJECT_STATUS_HOLD, project.status)
            # otestujeme, že se odelslal email zákazníkovi s potvrzením zadáním projektu
            self.assertEqual(1, len(mail.outbox))
            self.assertEqual(u.email, mail.outbox[0].to[0])

    def test_save_with_files(self):
        u = baker.make('users.User')
        f = baker.make('files.File', user=u)
        data = '{"name": "test", "description": "volitelná poznámka", "due_date": "2019-01-01", "status": 10,' \
               '"step1": 0, "step2": 10, "step3": 0, "step4": 10, "step5": 0, "step6": 10,' \
               ' "files": [%s]}' % f.id

        request = Request(HttpRequest())
        request.user = u
        serializer = WriteProjectSerialier(data=json.loads(data), context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=u)
        project = Project.objects.all().first()
        self.assertEqual(u.id, project.owner.id)
        self.assertEqual(f.id, project.files.all().first().id)

    def test_validate_files(self):
        u = baker.make('users.User')
        f = baker.make('files.File')
        p = baker.make('projects.Project')
        data = '{"files": [%s]}' % f.id

        request = Request(HttpRequest())
        request.user = u

        serializer = WriteProjectSerialier(p, data=json.loads(data), context={'request': request}, partial=True)
        self.assertFalse(serializer.is_valid())
        self.assertIn('files', serializer.errors.keys())
