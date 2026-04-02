#Aufgabe
#Definieren einer Funktion zur Berechnung der Gesamtkosten eines Produkts durch Multiplikation von Preis und verkaufter Menge.
#Erstellen einer Funktion mit dem Namen calculate_total_cost(), die zwei Parameter entgegennimmt: price und quantity.
#Innerhalb der Funktion wird price mit quantity multipliziert, um die Gesamtkosten zu berechnen.
#Rückgabe des Ergebnisses aus der Funktion.
#Ausgabebedingungen
#Aufruf von calculate_total_cost() mit price = 1.50 und quantity = 10.
#Ausgabe des Ergebnisses als:
#The total cost for apples is $<apples_total_cost>

# Call the function and print the result
def calculate_total_cost(price, quantity):
    apples_total_cost = price * quantity
    return apples_total_cost

apples_total_cost = calculate_total_cost(1.50, 10)

print(f"The total cost for apples is ${apples_total_cost}")
    