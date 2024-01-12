import json
from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        with open('data.json', "r", encoding="UTF-8") as file:
            data = json.load(file)

        products = []
        category = []
        for item in data:
            if item["model"] == "catalog.product":
                products.append(Product(**item['fields']))
            elif item["model"] == "catalog.category":
                category.append(Category(**item['fields']))


        Product.objects.bulk_create(products)
        Category.objects.bulk_create(category)


# from django.core.management import BaseCommand
# from catalog.models import Product, Category
#
#
# class Command(BaseCommand):
#     def handle(self, *args, **options):
#
#         product_list = [
#             {
#                 "name": "Air Jordan 11 Retro",
#                 "category": 1,
#                 "photo": "catalog/air_IPZhuKI.jpg",
#                 "price": 28000.0,
#                 "overview": "модель ретро",
#                 "created": "2024-01-09T17:50:53Z",
#                 "updated": "2024-01-09T17:51:50.024Z"
#             }
#         ]
#         Product.objects.all().delete()
#         Category.objects.all().delete()
#
#         products_for_create = []
#         for product_item in product_list:
#             category_id = product_item.pop('category')
#             category = Category.objects.get(id=category_id)
#             product_item['category'] = category
#             products_for_create.append(
#                 Product(**product_item)
#             )
#
#         Product.objects.bulk_create(products_for_create)


import json
from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        with open('data.json', "r", encoding="UTF-8") as file:
            data = json.load(file)

        products = []
        category = []
        for item in data:
            if item["model"] == "catalog.product":
                products.append(Product(**item['fields']))
            elif item["model"] == "catalog.category":
                category.append(Category(**item['fields']))


        Product.objects.bulk_create(products)
        Category.objects.bulk_create(category)






