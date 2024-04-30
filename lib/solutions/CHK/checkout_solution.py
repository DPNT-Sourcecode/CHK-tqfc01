

# noinspection PyUnusedLocal
# skus = unicode string

import re
import math

ALLOWED_SKUS = 'ABCDE'

PRICE_TABLE = [
    {'sku': 'A', 'price': 50},
    {'sku': 'B', 'price': 30},
    {'sku': 'C', 'price': 20},
    {'sku': 'D', 'price': 15},
    {'sku': 'E', 'price': 40}
]

OFFER_TABLE = {
    'A': [
        {'offer': 5, 'offer_price': 200},
        {'offer': 3, 'offer_price': 130}
    ],
    'B': [
        {'offer': 2, 'offer_price': 45}
    ],
    'E': [
        {'offer': 2, 'offer_price': 40}
    ]
}

def checkout(skus):
    if isinstance(skus, str) and bool(re.match(f'^[{ALLOWED_SKUS}]*$', skus)):
        total_sum = 0
        for row in PRICE_TABLE:
            sku = row.get('sku')
            count = skus.count(sku)

            if count:
                offer = row.get('offer')
                offer_sum = 0
                if offer and count >= offer:
                    offer_count = math.floor(count / offer)
                    count = count % offer
                    offer_sum = offer_count * row.get('offer_price', 0)
                
                count_sum = count * row.get('price', 0)

                total_sum = total_sum + count_sum + offer_sum
        return total_sum
    else:
        return -1

