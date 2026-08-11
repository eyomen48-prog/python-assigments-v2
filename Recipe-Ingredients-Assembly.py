home = ["un", "şeker", "yumurta"]
guest = ["şeker", "süt", "çikolata"]

birlesik = home + guest

sonuc = []
for eleman in birlesik:
    if eleman not in sonuc:
        sonuc.append(eleman)

print(sonuc)
