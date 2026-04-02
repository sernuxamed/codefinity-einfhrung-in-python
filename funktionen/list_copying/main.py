#Aufgabe
#Erstellen einer Funktion zur Anwendung eines 10%-Rabattes auf Produktpreise über $2.00, ohne die ursprüngliche Liste zu verändern.
#Definition einer Funktion apply_discount(prices), die eine Liste von Preisen entgegennimmt.
#Innerhalb der Funktion eine Kopie von prices erstellen und dieser prices_copy zuweisen.
#Mit einer for-Schleife und Index-Iteration (range(len(prices_copy))) die kopierte Liste durchlaufen.
#Wenn ein Preis größer als 2.00 ist, einen 10%-Rabatt anwenden.
#Die aktualisierte Liste prices_copy zurückgeben.
#Ausgabebedingungen
#Die Funktion soll die neue Liste mit rabattierten Preisen zurückgeben.
#Das Ergebnis ausgeben mit:
#Updated product prices: <$updated_prices>
#Hinweis
#Indexbasierte Iteration verwenden, um die Liste korrekt zu verändern: for index in range(len(prices)): verändert Elemente direkt, im Gegensatz zu for price in prices:.

def apply_discount(prices):
    prices_copy = prices.copy()
    for price in range(len(prices_copy)):
        if prices_copy[price] > 2:
            prices_copy[price] -= prices_copy[price] * 0.1
    return prices_copy

    



# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)

print(f"Updated product prices: ${updated_prices}")