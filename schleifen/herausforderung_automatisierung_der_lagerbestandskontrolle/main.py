#Aufgabe
#Verwalten Sie den Lagerbestand eines Lebensmittelgeschäfts, indem Sie Artikel mit einer while-Schleife nachfüllen und Rabatte basierend auf dem Lagerbestand anwenden. Sie verwenden Schleifen, um den Status jedes Artikels zu aktualisieren, geben jedoch nur eine einfache Verarbeitungsmeldung für jeden Artikel und eine abschließende Zusammenfassung aus.
#Regeln
#Verwenden Sie eine for-Schleife, um jeden Artikel im inventory-Dictionary zu durchlaufen.
#Für jeden Artikel ermitteln Sie den aktuellen Bestand, den Mindestbestand, die Nachfüllmenge und den Verkaufsstatus.
#Verwenden Sie eine while-Schleife, um den Artikel nachzufüllen, bis sein Bestand mindestens dem Mindestbestand entspricht.
#Erhöhen Sie den Bestand bei jeder Iteration um die Nachfüllmenge.
#Aktualisieren Sie den Bestandswert im Dictionary nach dem Nachfüllen.
#Nach dem Nachfüllen: Wenn der Bestand den discount_threshold überschreitet und der Artikel nicht im Angebot ist, setzen Sie den Verkaufsstatus im Dictionary auf True.
#Ausgabeanforderungen
#Vor Beginn der Schleife eine Zeile mit dem Wort Processing ausgeben (zum Beispiel: Processing started).
#Für jeden Artikel eine einzelne Zeile ausgeben: Processing [item name] (zum Beispiel: Processing Bread).
#Nachdem alle Artikel verarbeitet wurden, eine Zusammenfassungszeile mit dem Wort Processing ausgeben (zum Beispiel: Processing completed).
#Keine Details zum Nachfüllen oder zur Rabattvergabe ausgeben. Kein abschließender Lagerbericht. Nur die geforderten Verarbeitungszeilen ausgeben.





# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")
for index in inventory:
    print(f"Processing {index}")
    while inventory[index][0] < inventory[index][1]:
#        print(f"vorher:  {inventory[index][0]}")
        inventory[index][0] += inventory[index][2]
#        print(f"nachher:  {inventory[index][0]}")
    if inventory[index][0] > discount_threshold and not inventory[index][3]:
        inventory[index][3] = True
#        print(inventory[index][3])
#    print(inventory)
#    print(f"Processing {index} completed")
print("Processing completed")