prices = [29.99, 45.50, 12.75, 38.20]

discount_factor = [0.10, 0.20, 0.15, 0.05]
#Rabatt nach Position
#Anwenden von Rabattprozentsätzen auf Produktpreise basierend auf ihrer Position in der Liste durch Iteration über Indizes.
#Verwendung einer for-Schleife mit range() und len(), um durch die Indizes von prices zu iterieren.
#Anwenden von Rabatten basierend auf der Indexposition und Aktualisierung jedes Preises in der Liste prices: 10% für Index 0, 20% für Index 1, 15% für Index 2 und 5% für Index 3.
#Ausgabe von Updated price for item {index}: ${updated_price:.2f} für jeden Artikel.

for index in range(len(prices)):
    # Rabatt direkt auf die bestehende Liste anwenden
    prices[index] -= prices[index] * discount_factor[index]
    print(f"Updated price for item {index}: ${prices[index]:.2f}")