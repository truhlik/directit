import os
import json
from django.core.management.base import BaseCommand

from django.conf import settings
from django.db import transaction

from main.apps.categories.models import Category
from main.apps.tags.models import Tag


class Command(BaseCommand):
    help = 'Seed Tags'

    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, 'seeds', 'tags.json')
        with open(path, mode='r') as f:
            data = json.load(f)
            with transaction.atomic():
                self.process_data(data)

    def process_data(self, data):
        for key, value in data.items():
            category, created = self._create_category(key)

            for name in value:
                self._create_tag(name, category)

    def _create_category(self, name):
        print('Getting category name: {}'.format(name))
        return Category.objects.get_or_create(name=name)

    def _create_tag(self, name, category):
        print('Creating tag name: {}, category: {}'.format(name, category))
        tag = Tag.objects.create(name=name)
        if category:
            tag.categories.add(category)
