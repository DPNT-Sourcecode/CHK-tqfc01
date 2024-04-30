

# noinspection PyUnusedLocal
# skus = unicode string

import re

ALLOWED_SKUS = 'ABCD'

def checkout(skus):
    if isinstance(skus, str) and bool(re.match(f'^[{ALLOWED_SKUS}]+$', skus)):
        unique_skus = list(set(skus))
        for sku in unique_skus:
            count = skus.count(sku)
    else:
        return -1
