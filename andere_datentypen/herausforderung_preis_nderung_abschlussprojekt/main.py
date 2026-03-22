# Aufgabe
# Verwalten Sie einen Lebensmittelinventar mithilfe eines Dictionaries in Python. Führen Sie grundlegende Operationen durch: Preis aktualisieren, einen neuen Artikel hinzufügen, Bestand basierend auf einer Bedingung anpassen, optional einen Artikel anhand des Preises entfernen und einfache Statusmeldungen ausgeben.

# Dictionary erstellen
# Definieren Sie grocery_inventory mit den folgenden Artikeln und Details:
#"Milk": ("Dairy", 3.50, 8)
#"Eggs": ("Dairy", 5.50, 30)
#"Bread": ("Bakery", 2.99, 15)
#"Apples": ("Produce", 1.50, 50)

grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

# Preis prüfen und aktualisieren
#Preis von "Eggs" abrufen.
#Wenn der Preis größer als 5 ist, ausgeben:
#"Eggs are too expensive, reducing the price by $1."
#und den Preis um 1 senken.
#Andernfalls ausgeben:
#The price of Eggs is reasonable.

if grocery_inventory.get("Eggs")[1] > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = (
        grocery_inventory["Eggs"][0],
        grocery_inventory["Eggs"][1] -1,
        grocery_inventory["Eggs"][2]
    )
else:
    print("The price of Eggs is reasonable.")

#Neuen Artikel hinzufügen
#"Tomatoes" mit den Details hinzufügen: Kategorie "Produce", Preis 1.20, Bestand 30.
#Dann ausgeben:
#Inventory after adding Tomatoes: <grocery_inventory>

grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:",grocery_inventory)
    

#Bestand verwalten
#Bestand von "Milk" prüfen.
#Wenn dieser weniger als 10 beträgt, ausgeben:
#Milk needs to be restocked. Increasing stock by 20 units.
#und den Bestand um 20 erhöhen.
#Andernfalls ausgeben:
#Milk has sufficient stock.

if grocery_inventory.get("Milk")[2] <10:
    grocery_inventory["Milk"] = (
        grocery_inventory["Milk"][0],
        grocery_inventory["Milk"][1],
        grocery_inventory["Milk"][2] +20
)
    print("Milk needs to be restocked. Increasing stock by 20 units.")
else:
    print("Milk has sufficient stock.")

#Artikel anhand des Preises entfernen
#Wenn der Preis von "Apples" über 2 liegt, "Apples" entfernen und ausgeben:
#Apples removed from inventory due to high price.
if grocery_inventory.get("Apples")[1] > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

print("Updated inventory:",grocery_inventory)
