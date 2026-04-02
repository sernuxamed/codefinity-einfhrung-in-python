#Aufgabe
#Verarbeite Produktdaten aus einem Dictionary, in dem Preise und Mengen als Strings gespeichert sind. Ziel ist es, den Gesamtumsatz für jedes Produkt zu berechnen und zusammenfassende Statistiken zu erstellen.
#Verwende eine for-Schleife, um durch das products-Dictionary zu iterieren. Greife bei jeder Iteration sowohl auf den Produktnamen (den Schlüssel) als auch auf die zugehörigen Werte (die Liste mit Preis und Menge) zu. So kannst du jedes Produkt und dessen Daten einzeln verarbeiten;
#Für jedes Produkt:
#Konvertiere den Preis in einen float;
#Konvertiere die verkaufte Menge in einen int;
#Multipliziere beide Werte, um den Gesamtumsatz für dieses Produkt zu erhalten;
#Füge den Gesamtumsatz zur Liste total_sales_list hinzu.
#Verwende sum(), um die Gesamtsumme aller Umsätze zu berechnen.
#Weisen Sie die Gesamtsumme der Variablen total_sum zu.
#Verwenden Sie min() und max(), um die minimalen und maximalen Umsatzwerte zu ermitteln.
#Weisen Sie den Minimalwert der Variablen min_sales zu.
#Weisen Sie den Maximalwert der Variablen max_sales zu.
#Ausgabebedingungen
#Für jedes Produkt ausgeben:
#Total sales for <product>: $<total_sales>
#Nach der Verarbeitung aller Produkte ausgeben:
#Total sum of all sales: $<total_sum>
#Minimum sales: $<min_sales>
#Maximum sales: $<max_sales>




# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for product, values in products.items():
    price_str, qty_strg = values
    #print(price_str)
    #print(qty_strg)
    price = float(price_str)
    quantity = int(qty_strg)
    total_sales = price * quantity
    total_sales_list.append(total_sales)
    print(f"Total sales for {product}: ${total_sales}")

total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)

print(f"Total sum of all sales: ${total_sum}")
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")




