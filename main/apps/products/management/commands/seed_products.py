import os
import json
from django.core.management.base import BaseCommand

from django.conf import settings
from django.db import transaction

from main.apps.categories.models import Category
from main.apps.companies.models import Company
from main.apps.companies import constants
from main.apps.products.models import Product
from main.apps.tags.models import Tag
from main.apps.vendors.models import Vendor


class Command(BaseCommand):
    help = 'Seed products'
    # konvertováno pomocí http://beautifytools.com/excel-to-json-converter.php

    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, 'seeds', 'products_and_vendors.json')
        with open(path, mode='r') as f:
            data = json.load(f)
            with transaction.atomic():
                self.process_data(data)

    def process_data(self, data):
        for item in data:
            section_name = item["section"]
            category_name = item["category"]
            product_name = item["product"]
            tag_name = item["tag_name"]
            tag_id = item["tag_id"]
            vendor_name = item["vendor"]
            suppliers = item["supplier"]
            description = item["description"]

            section = Category.objects.get_or_create(name=section_name)[0]
            print(category_name)
            category = Category.objects.get_or_create(name=category_name, defaults={"parent": section})[0]

            # vytvářím Vendora
            vendor = None
            if vendor_name is not None and vendor_name != "":
                vendor = self.create_vendor(vendor_name)

            # vytvářím tag, pokud žádný neexistuje v DB pod stejným ID nebo name
            try:
                tag = Tag.objects.get(id=tag_id or 0)
            except Tag.DoesNotExist:
                tag = None

            if tag is None and tag_name is not None and tag_name != "":
                tag = Tag.objects.get_or_create(name=tag_name)[0]

            # vytvářím suppliers
            supplier_list = []
            for supplier in suppliers.split(";"):
                if supplier == "":
                    continue
                supplier_list.append(self.create_supplier(supplier, tag, category))

            # vytvářím produkt
            if product_name is not None and product_name != "":
                try:
                    product = Product.objects.get(name=product_name)
                    self.update_product(product, category, tag, supplier_list)
                except Product.DoesNotExist:
                    self.create_product(product_name, category, tag, supplier_list, vendor, description)

    def create_vendor(self, name):
        v = Vendor(name=name)
        v.save()
        return v

    def create_supplier(self, name, tag, category):
        c = Company(
            role=constants.COMPANY_ROLE_SUPPLIER,
            name=name,
            description="",
            email="",
            phone="",
            city="",
        )
        c.save()
        if tag:
            c.tags.add(tag)

        if category:
            c.categories.add(category)

        return c

    def create_product(self, name, category, tag, supplier_list, vendor, description):
        p = Product(
            name=name,
            vendor=vendor,
            description=description,
        )
        p.save()
        if category:
            p.categories.add(category)
        if tag:
            p.tags.add(tag)
        if len(supplier_list) > 0:
            p.suppliers.set(supplier_list)

        return p

    def update_product(self, product, category, tag, supplier_list):
        if len(supplier_list) > 0:
            for s in supplier_list:
                product.suppliers.add(s)

        if tag:
            product.tags.add(tag)

        if category:
            product.categories.add(category)
