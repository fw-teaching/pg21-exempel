
products = [
    { "name": "äpple", "price": 1 },
    { "name": "päron", "price": 1 },
    { "name": "banan", "price": 3 }
]

for p in products:
    if p['price'] > 2:
        print(f"{ p['name'] } kostar {p['price']} € (DYRT!)")
    else:
        print(f"{ p['name'] } kostar {p['price']} €")

for p in products:
    info = ""
    if p['price'] > 2:
        info = " (DYRT!)"
    print(f"{ p['name'] } kostar {p['price']} €{info}")

for p in products:
    info = '(DYRT!)' if p['price'] > 2 else ''
    print(f"{ p['name'] } kostar {p['price']} € {info}")

for p in products:
    print(f"{ p['name'] } kostar {p['price']} €{ ' (DYRT!)' if p['price'] > 2 else '' }")