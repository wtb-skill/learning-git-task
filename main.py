lista_zakupow = {
    'piekarnia': ['chleb', 'pączek', 'bułki'],
    'warzywniak': ['marchew', 'seler', 'rukola'],
}

lista_zakupow_cap = {key.capitalize(): [item.capitalize() for item in value] for key, value in lista_zakupow.items()}

print("Lista zakupów")
for store, rzeczy in lista_zakupow_cap.items():
    print(f"Idę do {store} i kupuję tam {rzeczy}")

count = sum(len(items) for items in lista_zakupow.values())

print(f"W sumie kupuję {count} produktów.")

print("To jest pierwsza zmiana, którą wyślę poprzez commit.")

