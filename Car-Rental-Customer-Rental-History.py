def add_rental(history, customer, rental):

    if customer not in history:
        history[customer] = []

    for existing_rental in history[customer]:
        if existing_rental["date"] == rental["date"] and existing_rental["plate"] == rental["plate"]:
            return f"UYARI: {customer} adlı müşteri {rental['date']} tarihinde {rental['plate']} plakalı aracı zaten kiralamış!"
    history[customer].append(rental)
    return f"Kiralama başarıyla eklendi: {customer} → {rental['plate']} {rental['date']}"

history = {}
print(add_rental(history, "Ahmet", {"date": "2026-02-18", "plate": "34ABC123", "days": 2}))
print(add_rental(history, "Ahmet", {"date": "2026-02-18", "plate": "34ABC123", "days": 1}))
print(add_rental(history, "Ahmet", {"date": "2026-02-18", "plate": "34ABC123", "days": 3}))
print(add_rental(history, "Ahmet", {"date": "2026-02-18", "plate": "34ABC123", "days": 2}))
print("n\Güncel history:", history)
for customer, rentals in history.items():
    print(f"{customer}: {rentals}")