lista_zakupow = {
    'piekarnia': ['chleb', 'pączek', 'bułki'],
    'warzywniak': ['marchew', 'seler', 'rukola'],
}

lista_zakupow_cap = {key.capitalize(): [item.capitalize() for item in value] for key, value in lista_zakupow.items()}

