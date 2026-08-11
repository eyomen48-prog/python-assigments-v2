answers = ["A", "B", "A", "C", "A", "B",]

frekans = {}
for answer in answers:
    if answer in frekans:
        frekans[answer] += 1
    else:
        frekans[answer] = 1

        toplam = len(answers)
sonuc = {}
for secenek, sayi in frekans.items():
    sonuc[secenek] = {"count": sayi, "pct": round((sayi / toplam) * 100, 2)}

print(sonuc)