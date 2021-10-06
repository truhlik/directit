from django.test import TestCase

from model_bakery import baker

from ..serializers import CallBackSerializer, ConsiergeSerializer, ITAssistantSerializer


class CallBackSerializersTestCase(TestCase):

    def setUp(self) -> None:
        super(CallBackSerializersTestCase, self).setUp()

    def test_consierge_serializer_keys(self):
        c1 = baker.make('callbacks.CallBackRequest')
        self.assertSetEqual(set(['id', 'callback_type', 'name', 'phone', 'time', 'note', 'tags']),
                            set(ConsiergeSerializer(c1).data.keys()))

    def test_callback_serializer_keys(self):
        c1 = baker.make('callbacks.CallBackRequest')
        self.assertSetEqual(set(['id', 'name', 'phone', 'time', 'note', 'tags']),
                            set(CallBackSerializer(c1).data.keys()))


class ITAssistantSerializerTestCase(TestCase):

    def setUp(self) -> None:
        super(ITAssistantSerializerTestCase, self).setUp()

    def test_keys(self):
        c1 = baker.make('callbacks.CallBackRequest')
        self.assertSetEqual(set(['id', 'assistant_type', 'name', 'phone', 'time', 'note', 'categories']),
                            set(ITAssistantSerializer(c1).data.keys()))

    def test_values(self):
        c1 = baker.make('callbacks.CallBackRequest')
        exp_data = {
            'id': c1.id,
            'assistant_type': c1.callback_type,
            'name': c1.name,
            'phone': c1.phone,
            'time': c1.time,
            'note': c1.note,
            'categories': [c.id for c in c1.categories.all()],
        }
        self.assertEqual(exp_data, ITAssistantSerializer(c1).data)

    def test_valid(self):
        data = {
            'assistant_type': 'SURVEY',
            'name': "test",
            'phone': '777000111',
            'time': None,
            'note': "test",
            'categories': [],
        }
        serializer = ITAssistantSerializer(data=data)
        self.assertTrue(serializer.is_valid(raise_exception=True))

