

# noinspection PyUnusedLocal
# skus = unicode string

import re

PRICE_TABLE = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 70,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 20,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,    
    "Y": 20,
    "Z": 21
}

ALLOWED_SKUS = "".join(PRICE_TABLE.keys())

OFFERS_TABLE = [
    {"offer": ["AAAAA"], "price": 200},
    {"offer": ["AAA"], "price": 130},
    {"offer": ["B", "EE"], "price": 80},
    {"offer": ["BB"], "price": 45},
    {"offer": ["FFF"], "price": 20},
    {"offer": ["HHHHHHHHHH"], "price": 80},
    {"offer": ["HHHHH"], "price": 45},
    {"offer": ["KK"], "price": 120},
    {"offer": ["NNN", "M"], "price": 120},
    {"offer": ["PPPPP"], "price": 200},
    {"offer": ["Q", "RRR"], "price": 150},
    {"offer": ["QQQ"], "price": 80},
    {"offer": ["UUUU"], "price": 120},
    {"offer": ["VVV"], "price": 130},
    {"offer": ["VV"], "price": 90}
]

def find_and_remove(needles, haystack):
    if any(n not in haystack for n in needles):
        return False, haystack
    for n in needles:
        haystack = haystack.replace(n, "", 1)
    return True, haystack

def remove_multibuy(haystack):
    temp_haystack = haystack
    found = 0
    while found < 3:
        if "Z" in temp_haystack:
            temp_haystack = temp_haystack.replace("Z", "", 1)
            found += 1
        elif "S" in temp_haystack:
            temp_haystack = temp_haystack.replace("S", "", 1)
            found += 1
        elif "T" in temp_haystack:
            temp_haystack = temp_haystack.replace("T", "", 1)
            found += 1
        elif "Y" in temp_haystack:
            temp_haystack = temp_haystack.replace("Y", "", 1)
            found += 1
        elif "X" in temp_haystack:
            temp_haystack = temp_haystack.replace("X", "", 1)
            found += 1
        else:
            return False, haystack
    return True, temp_haystack

def checkout(skus):
    if isinstance(skus, str) and bool(re.match(f"^[{ALLOWED_SKUS}]*$", skus)):
        skus = "".join(sorted(skus))
        total_sum = 0

        while True:
            multibuy_found, skus = remove_multibuy(skus)
            if multibuy_found:
                total_sum += 45
            else:
                break

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

