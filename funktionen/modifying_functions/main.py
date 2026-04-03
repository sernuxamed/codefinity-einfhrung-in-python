#Aufgabe
#Funktionen zur Berechnung der Gesamtkosten eines Produkts durch Anwendung von Rabatt und Steuer unter Verwendung von Schlüsselwortargumenten und Standardwerten für mehr Flexibilität erstellen.
#Definition von apply_discount(price, discount=0.05)
#→ Gibt den Preis nach Abzug des Rabatts zurück.
#Definition von apply_tax(price, tax=0.07)
#→ Gibt den Preis nach Hinzufügen der Steuer zurück.
#Definition von calculate_total(price, discount=0.05, tax=0.07)
#→ Verwendet apply_discount() und apply_tax(), um den Gesamtpreis mit sowohl Rabatt als auch Steuer zurückzugeben.
#Aufruf von calculate_total(120) mit dem Standardrabatt und der Standardsteuer.
#Aufruf von calculate_total(100, discount=0.10, tax=0.08) mit benutzerdefinierten Werten über Schlüsselwortargumente.
#Ausgabebedingungen
#Ausgabe des Ergebnisses mit Standardwerten:
#Total cost with default discount and tax: $<total_price_default>
#Ausgabe des Ergebnisses mit benutzerdefinierten Werten:
#Total cost with custom discount and tax: $<total_price_custom>
#Hinweis
#Bei der Definition von Funktionen sollten erforderliche Parameter zuerst und anschließend Parameter mit Standardwerten angegeben werden.
#Beim Aufruf von Funktionen mit Schlüsselwortargumenten müssen Positionsargumente vor Schlüsselwortargumenten stehen.


####

def apply_discount(price, discount=0.05):
    price = price - (discount * price)
    return price
    
#price = apply_discount(100)
#print(price)


def apply_tax(price, tax=0.07):
    price = price + (tax * price)
    return price

#price = apply_tax(price)
#print(price)

def calculate_total(price, discount=0.05, tax=0.07):
    price = apply_discount(price, discount)
    price = apply_tax(price, tax)
    return price

total_price_default = calculate_total(120)
print(f"Total cost with default discount and tax: ${total_price_default}")
total_price_custom = calculate_total(100, 0.10, 0.08)
print(f"Total cost with custom discount and tax: ${total_price_custom}")