import json
import os

from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        Category.objects.all().delete()

        path = os.path.join('catalog', 'fixtures', 'data.json')
        with open(path, "r", encoding="UTF-8") as file:
            data = json.load(file)

        category = []

        for item in data:

            if item["model"] == "catalog.category":
                category.append(Category(**item['fields']))
        Category.objects.bulk_create(category)








