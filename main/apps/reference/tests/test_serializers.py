from django.test import TestCase

from model_bakery import baker
from rest_framework.test import APIRequestFactory

from ..serializers import ReferenceSerializer, ReferenceWriteSerializer
from ...companies.constants import COMPANY_ROLE_SUPPLIER


class ReferenceSerializersTestCase(TestCase):

    def test_save(self):
        category = baker.make('categories.Category')
        company = baker.make('companies.Company', role=COMPANY_ROLE_SUPPLIER)
        p1 = baker.make('products.Product')
        p2 = baker.make('products.Product')

        data = {
          "category": category.id,
          "products": [p1.id, p2.id],
          "sector": 1,
          "title": "string",
          "contact_name": "string",
          "contact_email": "user@example.com",
          "problem_text": "string",
          "solution_text": "string",
          "benefits_text": "string"
        }
        factory = APIRequestFactory()
        user = baker.make('users.User')
        company.owners.add(user)
        request = factory.post('/')
        request.user = user

        serializer = ReferenceWriteSerializer(data=data, context={'request': request})
        self.assertTrue(serializer.is_valid(raise_exception=True))
        obj = serializer.save()
        self.assertEqual(category.id, obj.category.id)
        self.assertEqual(company.id, obj.solver.id)

    def test_values(self):
        category = baker.make('categories.Category', name='test kategory')
        company = baker.make('companies.Company', role=COMPANY_ROLE_SUPPLIER)
        user = baker.make('users.User')
        company.owners.add(user)

        obj = baker.make('reference.Reference',
                         title='ref projekt',
                         client_name='lubos',
                         category=category,
                         sector=1,
                         contact_name='kontakt name',
                         contact_email='kontakt email',
                         problem_text='problem',
                         solution_text='solution',
                         benefits_text='benefits',
                         owner=user,
                         )

        factory = APIRequestFactory()


        request = factory.post('/')
        request.user = user

        serializer = ReferenceSerializer(instance=obj, context={'request': request})
        exp_data = {
            "id": obj.id,
            "client_name": "lubos",
            "solver_obj": None,
            "category": category.id,
            "category_obj": {
                "name": 'test kategory',
                "id": category.id,
            },
            "products": [],
            "products_obj": [],
            "sector": 1,
            "sector_obj": {
                "id": 1,
                "name": "Bankovnictví, Finanční služby"
            },
            "title": 'ref projekt',
            "contact_name": 'k***',
            "contact_email": 'k***',
            "problem_text": 'problem',
            "solution_text": 'solution',
            "benefits_text": 'benefits',
            "files": [],
            "files_obj": [],
            "can_edit": True,
        }
        self.assertEqual(exp_data, serializer.data)