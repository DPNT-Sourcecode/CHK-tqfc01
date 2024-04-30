

# noinspection PyUnusedLocal
# skus = unicode string

import re

PRICE_TABLE = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10
}

ALLOWED_SKUS = "".join(PRICE_TABLE.keys())

OFFERS_TABLE = [
    {"offer": ["AAAAA"], "price": 200},
    {"offer": ["AAA"], "price": 130},
    {"offer": ["B", "EE"], "price": 80},
    {"offer": ["BB"], "price": 45},
    {"offer": ["FFF"], "price": 20}
]

def find_and_remove(needles, haystack):
    if any(n not in haystack for n in needles):
        return False, haystack
    for n in needles:
        haystack = haystack.replace(n, "", 1)
    return True, haystack

def checkout(skus):
    if isinstance(skus, str) and bool(re.match(f"^[{ALLOWED_SKUS}]*$", skus)):
        skus = "".join(sorted(skus))
        total_sum = 0

        for row in OFFERS_TABLE:
            while True:
                offer_found, skus = find_and_remove(row.get("offer", ""), skus)
                if offer_found:
                    total_sum += row.get("price", 0)
                else:
                    break

        for sku in skus:
            total_sum += PRICE_TABLE.get(sku, 0)

        return total_sum
    else:
        return -1




