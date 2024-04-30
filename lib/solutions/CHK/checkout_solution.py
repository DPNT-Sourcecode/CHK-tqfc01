

# noinspection PyUnusedLocal
# skus = unicode string

import re
# import math

ALLOWED_SKUS = 'ABCDE'

PRICE_TABLE = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40
}

OFFERS_TABLE = [
    {'offer': 'AAAAA', 'price': 200},
    {'offer': 'AAA', 'price': 130},
    {'offer': 'BEE', 'price': 80},
    {'offer': 'BB', 'price': 45}
]

def find_and_remove(needles, haystack):
    if any(n not in haystack for n in needles):
        return False
    for n in needles:
        haystack.replace(n, '', 1)
    return True

def checkout(skus):
    if isinstance(skus, str) and bool(re.match(f'^[{ALLOWED_SKUS}]*$', skus)):
        skus = ''.join(sorted(skus))
        total_sum = 0
        for row in OFFERS_TABLE:
            while True:
                index = skus.find(row.get('offer'))
                if index > -1:
                    skus = skus[:index] + skus[index + 1:]
                    total_sum += row.get('price')
                else:
                    break
        for sku in skus:
            total_sum += PRICE_TABLE.get(sku, 0)

        # total_sum = 0
        # for price_row in PRICE_TABLE:
        #     sku = price_row.get('sku')
        #     count = skus.count(sku)

        #     if count:
        #         offers = OFFER_TABLE.get(sku, [])
        #         for offer_row in offers:
        #             offer = offer_row.get('offer')
        #             if count >= offer:
        #                 offer_count = math.floor(count / offer)
        #                 count = count % offer
        #                 total_sum += offer_count * offer_row.get('offer_price', 0)
                
        #         total_sum += count * price_row.get('price', 0)
        return total_sum
    else:
        return -1

