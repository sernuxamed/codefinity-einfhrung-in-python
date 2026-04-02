#Aufgabe
#Sie erhalten zwei Listen mit Lebensmitteln:
#produce, die Obst und Gemüse enthält
#dairy, die Milchprodukte enthält
#Ihre Aufgabe ist es, diese beiden Listen zu einer einzigen Liste namens groceries zu kombinieren, wobei jede der ursprünglichen Listen ein Element innerhalb von groceries wird.
#Verwenden Sie anschließend verschachtelte for-Schleifen, um den Namen jedes Artikels auszugeben:
#Die äußere Schleife soll jede Kategorie (genannt section) in groceries durchlaufen.
#Die innere Schleife soll jedes item innerhalb der aktuellen section durchlaufen.
#Geben Sie jeden Artikel in folgendem Format in einer eigenen Zeile aus: Item name: <item>


produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce] + [dairy]
print(groceries)

for section in groceries:
#    print(section)
    for item in section:
        print("Item name: " + item)
    