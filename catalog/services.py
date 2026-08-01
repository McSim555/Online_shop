from django.core.cache import cache

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED


def get_products_list_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products, 10)
    return products


def get_product_of_category_from_cache(category_id):
    if not CACHE_ENABLED:
        return Product.objects.filter(category_id=category_id)
    key = f"product_of_category_{category_id}"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.filter(category_id=category_id)
    cache.set(key, products, 10)
    return products
