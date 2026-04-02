#Aufgabe
#Bewerten Sie die Artikel im inventory-Dictionary und geben Sie entsprechende Meldungen basierend auf deren Lagerbestand und Preisgestaltung aus.
#Iterieren Sie durch jeden Artikel im inventory-Dictionary.
#Für jeden Artikel:
#Wenn der Lagerbestand unter 30 liegt, geben Sie aus, dass er nachbestellt werden muss.
#Wenn der Lagerbestand über 100 liegt, geben Sie aus, dass er zum reduzierten Preis verkauft werden soll.
#Wenn der Lagerbestand zwischen 30 und 100 liegt, geben Sie aus, dass er zum regulären Preis verkauft werden soll.
#Ausgabebedingungen
#Verwenden Sie die folgenden Vorlagen für Ausgaben exakt:
#Für Nachbestellung:
#f"{item} need restocking."
#Für reduzierten Preis:
#f"{item} should be sold at the discounted price of {discounted_price}."
#Für regulären Preis:
#f"{item} should be sold at the regular price of {regular_price}."
#Hinweis
#Halten Sie sich exakt an die vorgegebenen Ausgabefomate, damit Ihre Lösung akzeptiert wird.



# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}

for item in inventory:
    if inventory[item][0] < 30:
        print(f"{item} need restocking.")
    elif inventory[item][0] > 100:
        discounted_price = inventory[item][2]
        print(f"{item} should be sold at the discounted price of {discounted_price}.")
    else:
        regular_price = inventory[item][1]
        print(f"{item} should be sold at the regular price of {regular_price}.")