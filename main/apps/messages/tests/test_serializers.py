from django.test import TestCase

from model_bakery import baker
from rest_framework.test import APIRequestFactory, force_authenticate

from ..models import MessageThread
from ..serializers import MessageSerializer
from ...companies.constants import COMPANY_ROLE_CONSULTANT, PROFILE_BASIC


class MessageSerializerTestCase(TestCase):

    def setUp(self) -> None:
        super(MessageSerializerTestCase, self).setUp()

    def test_valid_with_parent(self):
        user = baker.make('users.User')
        project = baker.make('projects.Project', owner=user)
        message = baker.make('custom_messages.Message', thread=MessageThread.objects.get(object_id=project.id))

        factory = APIRequestFactory()

        request = factory.get('/')
        force_authenticate(request, user=user)
        request.user = user

        data = {
            'thread_ct_id': project.id,
            'text': "test",
            'parent': message.id,
        }
        serializer = MessageSerializer(data=data, context={'request': request})
        self.assertTrue(serializer.is_valid(raise_exception=True))

    def test_valid(self):
        user = baker.make('users.User')
        project = baker.make('projects.Project', owner=user)

        factory = APIRequestFactory()

        request = factory.get('/')
        force_authenticate(request, user=user)
        request.user = user

        data = {
            'thread_ct_id': project.id,
            'text': "test",
            'parent': None,
        }
        serializer = MessageSerializer(data=data, context={'request': request})
        self.assertTrue(serializer.is_valid(raise_exception=True))

    def test_valid_with_consultant_user(self):
        user = baker.make('users.User')
        company = baker.make('companies.Company')
        company.owners.add(user)

        project = baker.make('projects.Project', consultant=company)

        factory = APIRequestFactory()

        request = factory.get('/')
        force_authenticate(request, user=user)
        request.user = user

        data = {
            'thread_ct_id': project.id,
            'text': "test",
            'parent': None,
        }
        serializer = MessageSerializer(data=data, context={'request': request})
        self.assertTrue(serializer.is_valid(raise_exception=True))

    def test_valid_with_supplier_user(self):
        user = baker.make('users.User')
        company = baker.make('companies.Company')
        company.owners.add(user)

        project = baker.make('projects.Project', supplier=company)

        factory = APIRequestFactory()

        request = factory.get('/')
        force_authenticate(request, user=user)
        request.user = user

        data = {
            'thread_ct_id': project.id,
            'text': "test",
            'parent': None,
        }
        serializer = MessageSerializer(data=data, context={'request': request})
        self.assertTrue(serializer.is_valid(raise_exception=True))

    def test_valid_wrong_user(self):
        user = baker.make('users.User')
        project = baker.make('projects.Project')

        factory = APIRequestFactory()

        request = factory.get('/')
        force_authenticate(request, user=user)
        request.user = user

        data = {
            'thread_ct_id': project.id,
            'text': "test",
            'parent': None,
        }
        serializer = MessageSerializer(data=data, context={'request': request})
        self.assertFalse(serializer.is_valid(raise_exception=False))
        self.assertIn('thread_ct_id', serializer.data.keys())

    def test_valid_wrong_thread_id(self):
        user = baker.make('users.User')
        project = baker.make('projects.Project', owner=user)

        factory = APIRequestFactory()

        request = factory.get('/')
        force_authenticate(request, user=user)
        request.user = user

        data = {
            'thread_ct_id': 0,
            'text': "test",
            'parent': None,
        }
        serializer = MessageSerializer(data=data, context={'request': request})
        self.assertFalse(serializer.is_valid(raise_exception=False))
        self.assertIn('thread_ct_id', serializer.data.keys())

    def test_valid_change_thread_id(self):
        user = baker.make('users.User')
        project = baker.make('projects.Project', owner=user)
        project2 = baker.make('projects.Project', owner=user)
        message = baker.make('custom_messages.Message', thread=MessageThread.objects.get(object_id=project.id))

        factory = APIRequestFactory()

        request = factory.get('/')
        force_authenticate(request, user=user)
        request.user = user

        data = {
            'thread_ct_id': project2.id,
            'text': "test",
            'parent': None,
        }
        serializer = MessageSerializer(instance=message, data=data, context={'request': request})
        self.assertFalse(serializer.is_valid(raise_exception=False))
        self.assertIn('thread_ct_id', serializer.data.keys())

    def test_validate_parent(self):
        user = baker.make('users.User')
        project = baker.make('projects.Project', owner=user)

        factory = APIRequestFactory()

        request = factory.get('/')
        force_authenticate(request, user=user)
        request.user = user

        data = {
            'thread_ct_id': project.id,
            'text': "test",
            'parent': 1,
        }
        serializer = MessageSerializer(data=data, context={'request': request})
        self.assertFalse(serializer.is_valid(raise_exception=False))

    def test_save_with_parent(self):
        user = baker.make('users.User')
        project = baker.make('projects.Project', owner=user)
        thread = MessageThread.objects.get(object_id=project.id)
        message = baker.make('custom_messages.Message', thread=thread)

        factory = APIRequestFactory()

        request = factory.get('/')
        force_authenticate(request, user=user)
        request.user = user

        data = {
            'thread_ct_id': project.id,
            'text': "test",
            'parent': message.id,
        }
        serializer = MessageSerializer(data=data, context={'request': request})
        self.assertTrue(serializer.is_valid(raise_exception=True))
        instance = serializer.save()
        self.assertTrue(instance.id)
        self.assertEqual(thread, instance.thread)
        self.assertEqual(message, instance.parent)

    def test_values(self):
        company = baker.make('companies.Company', name='test', role=COMPANY_ROLE_CONSULTANT, plan=PROFILE_BASIC)
        user = baker.make('users.User', first_name='Luboš', last_name='Truhlář', email='a@a.cz', phone='777000111')
        company.owners.set([user])
        project = baker.make('projects.Project', owner=user)
        thread = MessageThread.objects.get(object_id=project.id)
        message = baker.make('custom_messages.Message', thread=thread, text='ahoj', owner=user)
        c = baker.make('custom_messages.Message', thread=thread, text='ahoj', owner=user, parent=message)

        serializer = MessageSerializer(instance=message)
        exp_data = {
            'id': message.id,
            'owner': {
                'id': str(user.id),
                'first_name': "Luboš",
                'last_name': "Truhlář",
                'email': "a@a.cz",
                'phone': "777000111",
                'role': COMPANY_ROLE_CONSULTANT,
                'plan': PROFILE_BASIC,
            },
            'thread_ct_id': project.id,
            'text': "ahoj",
            'parent': None,
            'created_at': message.created_at.isoformat(),
            'updated_at': message.updated_at.isoformat(),
            'replies': 1,
        }
        self.assertEqual(exp_data, serializer.data)
