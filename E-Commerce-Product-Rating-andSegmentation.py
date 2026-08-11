products = [
    {"sku": "SKU1", "sales": 120, "return_rate": 0.05, "margin": 0.30},
    {"sku": "SKU2", "sales": 80, "return_rate": 0.2, "margin": 0.45},
    {"sku": "SKU3", "sales": 200, "return_rate": 0.05, "margin": 0.25}
]

for p in products:
    score = p["sales"] * p["margin"] - p["return_rate"] * 100
    p["score"] = score

products = sorted(products, key=lambda x: x["score"], reverse=True)


for p in products:
    if p["score"] >= 50:
        p["segment"] = "A"
    elif p["score"] >= 20:
        p["segment"] = "B"
    else:
        p["segment"] = "C"
for p in products:
    print(f"SKU: {p['sku']} | Score: {p['score']:.2f} | Segment: {p['segment']}")