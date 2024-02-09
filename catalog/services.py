from django.core.cache import cache

from catalog.models import Category
from config import settings


def get_categories_cache():
    if settings.CACHE_ENABLED:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            print(category_list)
            cache.set(key, category_list)
    else:
        category_list = Category.objects.all()

        return category_list