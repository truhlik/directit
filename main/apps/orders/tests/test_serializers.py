from django.test import TestCase
from rest_framework import serializers
from model_bakery import baker

from main.apps.companies import constants as company_consts
from ..serializers import OrderSerializer
from .. import constants


class OrderSerializersTestCase(TestCase):

    def setUp(self) -> None:
        super(OrderSerializersTestCase, self).setUp()

    def test_serializer_keys(self):
        c1 = baker.make('orders.Order')
        self.assertSetEqual(set(['id',
                                 'company',
                                 'rel_name',
                                 'company_obj',
                                 'date_from',
                                 'duration_length',
                                 'duration_unit',
                                 'note',
                                 'products',
                                 'categories',
                                 'files'
                                 ]),
                            set(OrderSerializer(c1).data.keys()))

    def test_validation_duration_unit_not_defined(self):
        c1 = baker.make('companies.Company', role=company_consts.COMPANY_ROLE_CONSULTANT)
        data = {"company": c1.id, "duration_length": 2}
        with self.assertRaises(serializers.ValidationError):
            OrderSerializer(data=data).is_valid(raise_exception=True)

    def test_validation_duration_length_not_defined(self):
        c1 = baker.make('companies.Company', role=company_consts.COMPANY_ROLE_CONSULTANT)
        data = {"company": c1.id, "duration_unit": constants.MONTH}
        with self.assertRaises(serializers.ValidationError):
            OrderSerializer(data=data).is_valid(raise_exception=True)

    def test_validation_without_company_fail(self):
        c1 = baker.make('companies.Company', role=company_consts.COMPANY_ROLE_CONSULTANT)
        data = {"duration_unit": constants.MONTH}
        with self.assertRaises(serializers.ValidationError):
            OrderSerializer(data=data).is_valid(raise_exception=True)

    def test_validation_duration_properly_set(self):
        c1 = baker.make('companies.Company', role=company_consts.COMPANY_ROLE_CONSULTANT)
        data = {"company": c1.id, "duration_unit": constants.MONTH, "duration_length": 2}
        self.assertTrue(OrderSerializer(data=data).is_valid())

    def test_validation_categories_and_missing_company(self):
        c1 = baker.make('categories.Category', name='endevel')
        data = {"categories": [c1.id]}
        self.assertTrue(OrderSerializer(data=data).is_valid())

    def test_validation_products_and_missing_company(self):
        t1 = baker.make('products.Product', name='endevel')
        data = {"products": [t1.id]}
        self.assertTrue(OrderSerializer(data=data).is_valid())

    def test_values_company_obj_consultant(self):
        c1 = baker.make('companies.Company', role=company_consts.COMPANY_ROLE_CONSULTANT, name='Luboš Truhlář')
        o1 = baker.make('orders.Order', company=c1)
        serializer = OrderSerializer(o1)
        self.assertIn('company_obj', serializer.data)
        self.assertEqual('***', serializer.data['company_obj']['phone'])
        self.assertEqual('***', serializer.data['company_obj']['email'])
        self.assertEqual('Luboš T*****', serializer.data['company_obj']['name'])

    def test_values_company_obj_supplier(self):
        c1 = baker.make('companies.Company', role=company_consts.COMPANY_ROLE_SUPPLIER,
                        name='Luboš Truhlář', email='a@a.cz', phone='777000112')
        o1 = baker.make('orders.Order', company=c1)
        serializer = OrderSerializer(o1)
        self.assertIn('company_obj', serializer.data)
        self.assertEqual('777000112', serializer.data['company_obj']['phone'])
        self.assertEqual('a@a.cz', serializer.data['company_obj']['email'])
        self.assertEqual('Luboš Truhlář', serializer.data['company_obj']['name'])

    def test_values_rel_name_with_company(self):
        c1 = baker.make('companies.Company', role=company_consts.COMPANY_ROLE_SUPPLIER,
                        name='Luboš Truhlář', email='a@a.cz', phone='777000112')
        o1 = baker.make('orders.Order', company=c1)
        serializer = OrderSerializer(o1)
        self.assertEqual('Luboš Truhlář', serializer.data['rel_name'])

    def test_values_rel_name_without_company(self):
        o1 = baker.make('orders.Order')
        serializer = OrderSerializer(o1)
        self.assertEqual('', serializer.data['rel_name'])

    def test_values_rel_name_without_company_with_categories_and_products(self):
        t1 = baker.make('products.Product', name='produkt1')
        t2 = baker.make('products.Product', name='produkt2')
        c1 = baker.make('categories.Category', name='cat1')
        c2 = baker.make('categories.Category', name='cat2')
        o1 = baker.make('orders.Order')
        o1.products.set([t1, t2])
        o1.categories.set([c1, c2])
        serializer = OrderSerializer(o1)
        self.assertEqual('produkt1, produkt2, cat1, cat2', serializer.data['rel_name'])
