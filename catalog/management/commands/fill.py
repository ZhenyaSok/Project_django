from django.core.management import  BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        products_list = [
                      {
                        "model": "catalog.product",
                        "pk": 3,
                        "fields": {
                          "name": "Air Jordan 11 Retro",
                          "category": 1,
                          "photo": "catalog/air_IPZhuKI.jpg",
                          "price": 28000.0,
                          "overview": "модель ретро",
                          "created": "2024-01-09T17:50:53Z",
                          "updated": "2024-01-09T17:51:50.024Z"
                        }
                      }
                    ]
        for product_item in products_list:
            Product.objects.create(**product_item)

        # products_for_create = []
        # for product_item in products_list:
        #     products_for_create.append(Product(**product_item))
        #
        # print(products_for_create)
        #
        # Product.object.bulk_create(products_for_create)


