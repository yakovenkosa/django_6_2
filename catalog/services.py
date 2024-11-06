from django.core.cache import cache
from config.settings import CACHES_ENABLED
from catalog.models import Product


def get_product_from_cache():
    if not CACHES_ENABLED:
        return Product.objects.all()
    key = "product_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_products_by_category(category_id):
    return Product.objects.filter(category_id=category_id)