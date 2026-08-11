attendance = [
    {"student": "Ali", "lesson": "Python", "minutes": 45},
    {"student": "Ali", "lesson": "SQL", "minutes": 30},
    {"student": "Ayşe", "lesson": "Python", "minutes": 60},
    {"student": "Ali", "lesson": "Python", "minutes": 15},
]
print(attendance)
öğrenci_toplam = {}
ders_toplam = {}
for kayit in attendance:
    isim = kayit["student"]
    ders = kayit["lesson"]
    dakika = kayit["minutes"]
    öğrenci_toplam[isim] = öğrenci_toplam.get(isim, 0) + dakika
    ders_toplam[ders] = ders_toplam.get(ders, 0) + dakika
    print(ders_toplam)
    print(öğrenci_toplam)