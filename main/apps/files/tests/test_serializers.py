from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import HttpRequest
from django.test import TestCase

from model_bakery import baker
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory, force_authenticate

from ..models import File
from ..serializers import FileSerializer


class CompanySerializersTestCase(TestCase):
    maxDiff = None

    def setUp(self) -> None:
        super(CompanySerializersTestCase, self).setUp()

    def test_keys(self):
        c1 = baker.make('files.File')
        self.assertSetEqual(set(['id', 'file', 'title', 'description']),
                            set(FileSerializer(c1).data.keys()))

    def test_valid_success(self):
        video = SimpleUploadedFile("file.txt", b"file_content", content_type="text/plain")
        data = {
            'title': 'test',
            'file': video,
            'description': 'test',
        }
        serializer = FileSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_valid_failed(self):
        data = {
            'title': 'test',
        }
        serializer = FileSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_save(self):
        video = SimpleUploadedFile("file.txt", b"file_content", content_type="text/plain")

        request = Request(HttpRequest())
        request.user = baker.make('users.User')

        data = {
            'title': 'test',
            'file': video,
            'description': 'desc',
        }
        serializer = FileSerializer(data=data, context={'request': request})
        serializer.is_valid()
        serializer.save()
        file = File.objects.all().first()
        self.assertEqual(file.title, 'test')
        self.assertEqual('file.txt', file.file.name.split('/')[1])
        self.assertEqual(request.user, file.user)

    def test_data(self):
        video = SimpleUploadedFile("file.txt", b"file_content", content_type="text/plain")
        file_obj = baker.make('files.File', file=video, title='test', description='desc')

        factory = APIRequestFactory()
        user = baker.make('users.User')

        # Make an authenticated request to the view...
        request = factory.get('/files/file/')
        force_authenticate(request, user=user)

        serializer = FileSerializer(file_obj, context={'request': request})
        exp_data = {
            'id': file_obj.id,
            'file': 'http://testserver/media/{}'.format(file_obj.file.name),
            'title': 'test',
            'description': 'desc',
        }
        self.assertEqual(exp_data, serializer.data)
