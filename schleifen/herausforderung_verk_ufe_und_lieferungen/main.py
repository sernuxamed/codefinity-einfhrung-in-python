#Aktualisierung der Produktlagerbestände basierend auf Verkäufen und Lieferungen mithilfe von Schleifen.
#Verwendung einer for-Schleife mit Indexiteration, um die products-Liste zu durchlaufen.
#Für jedes Produkt wird die Anzahl der verkauften Einheiten (units_sold) vom Lagerbestand des products abgezogen.
#Verwendung einer zweiten for-Schleife (ebenfalls mit Indexiteration), um die products erneut zu durchlaufen.
#Hinzufügen des entsprechenden Werts aus shipment_received, um den Lagerbestand zu aktualisieren.
#Am Ende ausgeben: Final stock levels for all products: <products>

# List of products with their initial stock levels at the start of the week
products = [
    ["Apples", 150],  
    ["Bananas", 200],
    ["Oranges", 100],
    ["Mangoes", 120]
]

# List of products sold by the end of the week
units_sold = [["Apples", 30], ["Bananas", 45], ["Oranges", 20], ["Mangoes", 10]]

# New shipment received at the end of the week
shipment_received = [["Apples", 50], ["Bananas", 70], ["Oranges", 30], ["Mangoes", 40]]

for index in range(len(units_sold)):
    products[index][1] -= units_sold[index][1]
#    print(products[index])

for index in range(len(shipment_received)):
    products[index][1] += shipment_received[index][1]
#    print(products[index])

print(f"Final stock levels for all products: {products}")