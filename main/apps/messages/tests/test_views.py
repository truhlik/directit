from django.urls import reverse

from model_bakery import baker
from rest_framework.test import APITestCase

from main.apps.companies import constants as company_consts
from ..models import Message, MessageThread


class MessagesViewsTestCase(APITestCase):

    def setUp(self) -> None:
        super(MessagesViewsTestCase, self).setUp()
        self.user = baker.make('users.User')
        c = baker.make('companies.Company', role=company_consts.COMPANY_ROLE_CLIENT, plan=company_consts.PROFILE_PREMIUM)
        c.owners.set([self.user])

    def do_auth(self):
        self.client.force_authenticate(user=self.user)

    def test_list(self):
        project = baker.make('projects.Project', owner=self.user)
        message1 = baker.make('custom_messages.Message', thread=MessageThread.objects.get(object_id=project.id))
        message3 = baker.make('custom_messages.Message', thread=MessageThread.objects.get(object_id=project.id), parent=message1)
        message2 = baker.make('custom_messages.Message')

        self.do_auth()
        resp = self.client.get(reverse('message-list'))
        self.assertEqual(200, resp.status_code)
        self.assertEqual(1, len(resp.data['results']))
        self.assertEqual(message1.id, resp.data['results'][0]['id'])
        self.assertEqual(1, resp.data['results'][0]['replies'])

    def test_list_filter_by_thread_id(self):
        project = baker.make('projects.Project', owner=self.user)
        project2 = baker.make('projects.Project', owner=self.user)
        message1 = baker.make('custom_messages.Message', thread=MessageThread.objects.get(object_id=project.id))
        message2 = baker.make('custom_messages.Message', thread=MessageThread.objects.get(object_id=project2.id))

        self.do_auth()
        resp = self.client.get(reverse('message-list') + '?thread__object_id={}'.format(project2.id))
        self.assertEqual(200, resp.status_code)
        self.assertEqual(1, len(resp.data['results']))
        self.assertEqual(message2.id, resp.data['results'][0]['id'])

    def test_list_filter_by_parent_id(self):
        project = baker.make('projects.Project', owner=self.user)
        project2 = baker.make('projects.Project', owner=self.user)
        message1 = baker.make('custom_messages.Message', thread=MessageThread.objects.get(object_id=project.id))
        message2 = baker.make('custom_messages.Message', thread=MessageThread.objects.get(object_id=project2.id), parent=message1)

        self.do_auth()
        resp = self.client.get(reverse('message-list') + '?parent={}'.format(message1.id))
        self.assertEqual(200, resp.status_code)
        self.assertEqual(1, len(resp.data['results']))
        self.assertEqual(message2.id, resp.data['results'][0]['id'])
