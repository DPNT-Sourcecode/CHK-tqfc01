

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
        for price_row in PRICE_TABLE:
            sku = price_row.get('sku')
            count = skus.count(sku)

            if count:
                offers = OFFER_TABLE.get(sku, [])
                for offer_row in offers:
                    offer = offer_row.get('offer')
                    if count >= offer:
                        offer_count = math.floor(count / offer)
                        count = count % offer
                        total_sum += offer_count * offer_row.get('offer_price', 0)
                
                total_sum += count * price_row.get('price', 0)
        return total_sum
    else:
        return -1


