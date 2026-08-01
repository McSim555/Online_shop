from catalog.models import Product
from config.settings import CACHE_ENABLED



def get_products_list():
    if not CACHE_ENABLED:
        return Product.objects.all()
    else: