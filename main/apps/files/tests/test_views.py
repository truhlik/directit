from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from model_bakery import baker
from rest_framework.test import APITestCase
from main.apps.companies import constants as company_constants


class FileViewSetTestCase(APITestCase):

    def setUp(self) -> None:
        super(FileViewSetTestCase, self).setUp()
        self.user = baker.make('users.User')
        c = baker.make('companies.Company', role=company_constants.COMPANY_ROLE_CLIENT, plan=company_constants.PROFILE_PREMIUM)
        c.owners.set([self.user])

    def do_auth(self):
        self.client.force_authenticate(user=self.user)

    def test_list_auth_only_success(self):
        self.do_auth()
        r = self.client.get(reverse('file-list'))
        self.assertEqual(200, r.status_code)

    def test_list_auth_only_failed(self):
        r = self.client.get(reverse('file-list'))
        self.assertEqual(401, r.status_code)

    def test_get_auth_only_success(self):
        self.do_auth()
        r = self.client.get(reverse('file-detail', args=(1, )))
        self.assertEqual(404, r.status_code)

    def test_get_auth_only_success_obj_exists(self):
        obj = baker.make('files.File', user=self.user)
        self.do_auth()
        r = self.client.get(reverse('file-detail', args=(obj.id, )))
        self.assertEqual(200, r.status_code)

    def test_get_auth_only_failed(self):
        r = self.client.get(reverse('file-detail', args=(1, )))
        self.assertEqual(401, r.status_code)

    def test_post_auth_only_success(self):
        self.do_auth()
        r = self.client.post(reverse('file-list'), data={})
        self.assertEqual(400, r.status_code)

    def test_post_auth_only_failed(self):
        r = self.client.get(reverse('file-list'), data={})
        self.assertEqual(401, r.status_code)

    def test_put_auth_only_success_obj_does_not_exist(self):
        self.do_auth()
        r = self.client.put(reverse('file-detail', args=(1, )), data={})
        self.assertEqual(404, r.status_code)

    def test_put_auth_only_success_obj_exists(self):
        video = SimpleUploadedFile("file.txt", b"file_content", content_type="text/plain")
        data = {
            'title': 'test',
            'file': video,
            'description': 'desc',
        }
        obj = baker.make('files.File', user=self.user)
        self.do_auth()
        r = self.client.put(reverse('file-detail', args=(obj.id, )), data=data)
        self.assertEqual(200, r.status_code)

    def test_put_auth_only_failed(self):
        video = SimpleUploadedFile("file.txt", b"file_content", content_type="text/plain")
        data = {
            'title': 'test',
            'file': video,
            'description': 'desc',
        }

        r = self.client.patch(reverse('file-detail', args=(1, )), data=data)
        self.assertEqual(401, r.status_code)
