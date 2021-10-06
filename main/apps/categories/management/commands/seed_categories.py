import os
import json
from django.core.management.base import BaseCommand

from django.conf import settings
from django.db import transaction

from main.apps.categories.models import Category


class Command(BaseCommand):
    help = 'Seed Categories'

    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, 'seeds', 'categories.json')
        with open(path, mode='r') as f:
            data = json.load(f)
            with transaction.atomic():
                self.process_data(data)

    def process_data(self, data, parent=None):
        for key, value in data.items():
            self._create_category(key, parent)

            # rekruze
            if type(value) == dict:
                self.process_data(value, key)

            if type(value) == list:
                for name in value:
                    self._create_category(name, key)

    def _create_category(self, name, parent=None):
        print('name: {}, parent: {}'.format(name, parent))
        if parent:
            parent = Category.objects.get(name=parent)
            Category.objects.create(name=name, parent=parent)
        else:
            Category.objects.create(name=name)
