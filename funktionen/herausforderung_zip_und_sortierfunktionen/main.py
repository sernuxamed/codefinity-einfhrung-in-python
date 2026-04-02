#Aufgabe
#Du hast drei Listen: Produktnamen, Preise und verkaufte Mengen. Deine Aufgabe ist es, diese Daten zu organisieren, zu sortieren und in einem bestimmten Format anzuzeigen.
#Code-Anweisungen
#Mit zip() die drei Listen zu einer Liste von Tupeln in der Reihenfolge (product_name, price, quantity_sold) kombinieren. Das Ergebnis in combined_list speichern.
#Mit sorted() die combined_list nach Produktnamen aufsteigend sortieren. Das sortierte Ergebnis in sorted_products speichern.
#Durch sorted_products iterieren und für jedes Produkt den Namen, Preis und die verkaufte Menge im angegebenen Format ausgeben.


# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

combined_list = list(zip(products, prices, quantities_sold))

sorted_products = sorted(combined_list)

print(sorted_products)

for product in sorted_products:
    print(f"Product: {product[0]}, Price: {product[1]}, Quantity Sold:{product[2]}")

