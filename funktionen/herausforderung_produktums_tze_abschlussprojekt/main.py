#Aufgabe
#Befolgen Sie diese schrittweisen Anweisungen, um die Aufgabe zu bearbeiten:
#Initialisieren Sie eine Liste namens products, die die Produktnamen enthält;
#Initialisieren Sie eine Liste namens prices, die den Stückpreis für jedes Produkt enthält;
#Initialisieren Sie eine Liste namens quantities_sold, die die Anzahl der verkauften Einheiten für jedes Produkt enthält;
#Berechnen Sie den Umsatz für jedes Produkt, indem Sie den Preis mit der verkauften Menge multiplizieren, und speichern Sie alle Ergebnisse in einer neuen Liste namens revenue;
#Verwenden Sie die Funktion zip(), um die Listen products und revenue zu einer Liste von Tupeln namens revenue_per_product zu kombinieren, wobei jedes Tupel einen Produktnamen und den entsprechenden Umsatz enthält;
#Sortieren Sie die Liste revenue_per_product alphabetisch nach Produktnamen;
#Geben Sie jedes Produkt und dessen Umsatz in folgendem Format aus: <product_name> has total revenue of $<revenue>.
#Sie müssen die folgenden Funktionen definieren:
#calculate_revenue(prices, quantities_sold): Diese Funktion soll jeden Preis mit der entsprechenden verkauften Menge multiplizieren, die Ergebnisse in einer Liste speichern und diese Liste der Umsätze zurückgeben.
#formatted_output(revenues): Diese Funktion soll eine Liste von (product_name, revenue)-Tupeln entgegennehmen, sie alphabetisch nach Produktnamen sortieren und jedes Element im angegebenen Format ausgeben.
#Nachdem Sie diese Funktionen definiert haben, verwenden Sie die bereitgestellten Listen, um sie aufzurufen und die Ergebnisse wie oben beschrieben anzuzeigen.

# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    revenue = []
    for item in range(len(prices)):
        revenue.append(prices[item] * quantities_sold[item])
    return revenue

#print(revenue)

def formatted_output(revenues):
    for product, amount in sorted(revenues):
        print(f"{product} has total revenue of ${amount}")

revenue_list = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenue_list))
formatted_output(revenue_per_product)


# Example of expected output line (do not remove):
print(" #### ")
#print(f"{revenue[0]} has total revenue of ${revenue[1]}")