bank = [
    {"category": "Maaş",     "amount": 30000},
    {"category": "Market",     "amount": -850},
    {"category": "Ulaşım",     "amount": -120},
    {"category": "Market",     "amount": -230},
]
kategori_toplam = {}
for hareket in bank:
    kategori = hareket["category"]
    tutar = hareket["amount"]
    if kategori in kategori_toplam:
        kategori_toplam[kategori] += tutar
    else:
        kategori_toplam[kategori] = tutar

        print(kategori_toplam)
giderler = {}
for kategori, toplam in kategori_toplam.items():
    if toplam < 0:
        giderler[kategori] = toplam

print(giderler)

net_bakiye = sum(kategori_toplam.values())
print(net_bakiye)
