customers = []
next_id = 1


def musteri_ekle():
    global next_id
    print("\n--- Müşteri Ekle ---")

    name = input("Ad Soyad: ")
    phone = input("Telefon: ")
    email = input("E-posta: ")
    city = input("Şehir: ")

    yeni_musteri = {
        "id": next_id,
        "name": name,
        "phone": phone,
        "email": email,
        "city": city,
    }

    customers.append(yeni_musteri)
    print(f"'{name}' eklendi. (ID: {next_id})")
    next_id += 1


def musteri_listele():
    print("\n--- Müşteri Listesi ---")

    if not customers:
        print("Henüz müşteri yok.")
        return

    for c in customers:
        print(f"[{c['id']}] {c['name']} | {c['phone']} | {c['email']} | {c['city']}")


def musteri_guncelle():
    print("\n--- Müşteri Güncelle ---")

    try:
        aranan_id = int(input("Güncellenecek müşteri ID: "))
    except ValueError:
        print("Geçersiz ID.")
        return

    for c in customers:
        if c["id"] == aranan_id:
            print(f"Mevcut Telefon: {c['phone']}")
            print(f"Mevcut E-posta: {c['email']}")

            yeni_phone = input("Yeni telefon (boş bırak değişmesin): ")
            yeni_email = input("Yeni e-posta (boş bırak değişmesin): ")

            if yeni_phone:
                c["phone"] = yeni_phone

            if yeni_email:
                c["email"] = yeni_email

            print("Müşteri güncellendi.")
            return

    print(f"ID {aranan_id} bulunamadı.")


def musteri_sil():
    print("\n--- Müşteri Sil ---")

    try:
        aranan_id = int(input("Silinecek müşteri ID: "))
    except ValueError:
        print("Geçersiz ID.")
        return

    for c in customers:
        if c["id"] == aranan_id:
            customers.remove(c)
            print(f"ID {aranan_id} silindi.")
            return

    print(f"ID {aranan_id} bulunamadı.")


def musteri_ara():
    print("\n--- İsimle Ara ---")

    kelime = input("Aranacak isim: ").lower()

    sonuclar = [c for c in customers if kelime in c["name"].lower()]

    if not sonuclar:
        print("Sonuç bulunamadı.")
    else:
        print(f"{len(sonuclar)} sonuç bulundu:")
        for c in sonuclar:
            print(f"[{c['id']}] {c['name']} | {c['city']}")


def sehir_raporu():
    print("\n--- Şehir Bazında Müşteri Sayısı ---")

    if not customers:
        print("Henüz müşteri yok.")
        return

    rapor = {}

    for c in customers:
        sehir = c["city"]
        if sehir in rapor:
            rapor[sehir] += 1
        else:
            rapor[sehir] = 1

    for sehir, adet in rapor.items():
        print(f"{sehir}: {adet} müşteri")


def menu():
    while True:
        print("""
1. Müşteri Ekle
2. Müşteri Listele
3. Müşteri Güncelle
4. Müşteri Sil
5. İsimle Ara
6. Şehir Raporu
7. Çıkış
""")

        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            musteri_ekle()
        elif secim == "2":
            musteri_listele()
        elif secim == "3":
            musteri_guncelle()
        elif secim == "4":
            musteri_sil()
        elif secim == "5":
            musteri_ara()
        elif secim == "6":
            sehir_raporu()
        elif secim == "7":
            print("Çıkış yapılıyor. Güle güle!")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")


menu()