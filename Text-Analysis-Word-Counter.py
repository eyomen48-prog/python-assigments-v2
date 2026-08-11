text = "Bugün hava çok güzel bugün dışarı çıkmak çok güzel"
kelimeler = text.split()
print(kelimeler)
frekans = {}
for kelime in kelimeler:
    if kelime in frekans:
        frekans[kelime] = frekans[kelime] + 1
    else:
        frekans[kelime] = 1

print(frekans)

sirali = sorted(frekans.items(), key=lambda x: x[1], reverse=True)
print(sirali)
print(sirali[:3])