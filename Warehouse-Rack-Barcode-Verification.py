def validate_barcode(barcode, warehouses):
    parts = barcode.split("X")
    all_digits = all(part.isdigit() for part in parts)

    if not all_digits:
        return "HATA: Barkod sadece sayısal değerler içermeli!"

    warehouse_id = int(parts[0])
    if warehouse_id not in warehouses:
        return "HATA: Depo bulunamadı!"

    return "Depo bulundu!"

warehouses = [12, 45, 7]
print(validate_barcode("12X3X2X5", warehouses))
print(validate_barcode("99X3X2X5", warehouses))
print(validate_barcode("12X3XaX5", warehouses))