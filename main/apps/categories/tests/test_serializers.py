from django.test import TestCase

from model_bakery import baker

from ..models import Category
from ..serializers import CategorySerializer, CategoryGroupingSerializer


class CategorySerializersTestCase(TestCase):

    def setUp(self) -> None:
        super(CategorySerializersTestCase, self).setUp()

    def test_category_serializer_keys(self):
        c1 = baker.make('tags.Tag')
        self.assertSetEqual(set(['id', 'name']),
                            set(CategorySerializer(c1).data.keys()))

    def test_category_annotated_values(self):
        c1 = baker.make('categories.Category', parent=None, name='test')
        c2 = baker.make('categories.Category', parent=c1, name='test2')
        c3 = baker.make('categories.Category', parent=c1, name='test3')
        baker.make('products.Product', categories=[c3])
        baker.make('products.Product', categories=[c3])
        with self.assertNumQueries(2):
            qs = Category.objects.main_category_with_prefetch_subcategories_and_projects()
            exp_data = [
                {
                    "id": c1.id,
                    "name": "test",
                    "subcategories": [
                        {
                            "id": c2.id,
                            "name": "test2",
                            "products_count": 0,
                        },
                        {
                            "id": c3.id,
                            "name": "test3",
                            "products_count": 2,
                        }
                    ]
                 }
            ]

            serializer = CategoryGroupingSerializer(qs, many=True)
            self.assertEqual(exp_data, serializer.data)
