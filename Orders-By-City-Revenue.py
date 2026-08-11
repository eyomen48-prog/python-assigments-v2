orders = [
    {"city": "istanbul", "total": 1200},
    {"city": "ankara", "total": 800},
    {"city": "izmir", "total": 500},
]
city_totals = {}
for order in orders:
    city = order["city"]
    total = order["total"]

    city_totals[city] = city_totals.get(city, 0) + total

    print(city_totals)
    en_yüksek_şehir = max(city_totals, key=city_totals.get)
    print(en_yüksek_şehir)
    print(en_yüksek_şehir, city_totals[en_yüksek_şehir])