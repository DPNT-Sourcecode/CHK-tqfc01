

# noinspection PyUnusedLocal
# skus = unicode string

import re
import math

ALLOWED_SKUS = [
    {'sku': 'A', 'price': 50, 'offer': 3, 'offer_price': 130},
    {'sku': 'B', 'price': 30, 'offer': 2, 'offer_price': 45},
    {'sku': 'C', 'price': 20},
    {'sku': 'D', 'price': 15}
]

def checkout(skus):
    if isinstance(skus, str) and bool(re.match(f'^[{ALLOWED_SKUS}]+$', skus)):
        for i in list(ALLOWED_SKUS):
            count = skus.count(i)
            if i == 'A' and count >= 3:
                offer_count = math.floor(count / 3)
                remainder = count % 3
            if i == 'A' and count >= 3:
                offer_count = math.floor(count / 3)
                remainder = count % 3


    else:
        return -1

