#Definieren eines Dictionaries grocery_inventory zur Speicherung der Informationen:
#"Milk": (113, "Dairy")
#"Eggs": (116, "Dairy")
#"Bread": (117, "Bakery")
#"Apples": (141, "Produce")

grocery_inventory = {
    "Milk": (113, "Dairy"),
    "Eggs": (116, "Dairy"),
    "Bread": (117, "Bakery"),
    "Apples": (141, "Produce")
}

# Abrufen der Details des Artikels "Bread" aus dem Dictionary und Speichern in der Variablen bread_details.
bread_details = grocery_inventory.get("Bread")
# Ausgabe der Details von "Bread": Details of Bread: <$bread_details>.
print("Details of Bread:",bread_details)

# Hinzufügen eines neuen Artikels, "Cookies", mit der Produkt-ID 143 und der Kategorie "Bakery".
grocery_inventory.update({"Cookies": (143, "Bakery")})

# Nach dem Hinzufügen von "Cookies" Ausgabe des aktualisierten Lagerbestands: Inventory after adding Cookies: <$grocery_inventory>.
print("Inventory after adding Cookies:", grocery_inventory)

#Entfernen des Artikels "Eggs" aus dem Dictionary.
grocery_inventory.pop("Eggs")

# Nach dem Entfernen von "Eggs" Ausgabe des aktualisierten Lagerbestands: Inventory after removing Eggs: <$grocery_inventory>.
print("Inventory after removing Eggs:",grocery_inventory)