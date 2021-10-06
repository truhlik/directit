import os
import csv

from django.core.management.base import BaseCommand

from django.conf import settings
from django.db import transaction

from main.apps.companies.models import Company
from main.apps.tags.models import Tag


class Command(BaseCommand):
    help = 'Seed Tags'

    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, 'seeds', 'tagy2.csv')
        with open(path, mode='r') as f:
            csvreader = csv.reader(f, delimiter=";")

            with transaction.atomic():
                for row in csvreader:
                    try:
                        orig_id = int(row[0])
                    except ValueError:
                        continue
                    new_name = row[2]
                    if new_name == "" or new_name == " ":
                        continue
                    if new_name == "XXX" or new_name == "X":
                        self.delete(orig_id)
                    self.process(orig_id, new_name)

    def process(self, orig_id: int, new_name: str):
        try:
            old_tag = Tag.objects.get(id=orig_id)
        except Tag.DoesNotExist:
            print(orig_id, new_name)
            return

        try:
            new_tag = Tag.objects.get(name__exact=new_name)

            # jedná se o stejný tag, tak nenahrazuju
            if new_tag.id == orig_id:
                return

            # jedná se o jiný tag, tak musím nahradit všechny vazby
            self.replace(old_tag, new_tag)
            old_tag.delete()

        except Tag.DoesNotExist:
            old_tag.name = new_name
            old_tag.save()

    def replace(self, old_tag: Tag, new_tag: Tag):
        for company in Company.objects.filter(tags=old_tag):
            company.tags.add(new_tag)
            company.tags.remove(old_tag)

    def delete(self, orig_id: int):
        try:
            old_tag = Tag.objects.get(id=orig_id)
            old_tag.delete()
        except Tag.DoesNotExist:
            return
