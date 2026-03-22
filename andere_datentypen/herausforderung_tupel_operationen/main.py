# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

# Aufgabe
# Verwalten eines Tupels, das ein Regal mit Obst darstellt, durch Ausführen von Operationen zum Zählen, Finden und Überprüfen der Lagerbestände.

#zählen, wie oft "apples" im Tupel shelf vorkommen. Dies in apple_count speichern und ausgeben: "Number of Apples: <$apple_count>".

apple_count = shelf.count("apples")
# Ausgabe der Anzahl der Äpfel: "Number of Apples: <$apple_count>".
print("Number of Apples:", apple_count)

# Ermitteln des Index des ersten Vorkommens von "bananas" im Tupel shelf. Den Index in banana_index speichern und ausgeben: "First Banana Index: <$banana_index>".
banana_index = shelf.index("bananas")
#Ausgabe des Index des ersten Vorkommens von Bananen: "First Banana Index: <$banana_index>".
print("First Banana Index:", banana_index)

# Überprüfen, ob die Anzahl der Äpfel kleiner als 5 ist. Falls ja, ausgeben: "Apples need to be restocked." Andernfalls ausgeben: "Apples are sufficiently stocked."
# Ausgabe einer Nachricht zum Apfelbestand: "Apples need to be restocked." oder "Apples are sufficiently stocked."
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")

# Zählen, wie oft "grapes" im Tupel shelf vorkommen. Falls Trauben nur einmal vorkommen, ausgeben: "Grapes need to be restocked." Andernfalls ausgeben: "Grapes are sufficiently stocked."
# Ausgabe einer Nachricht zum Traubenbestand: "Grapes need to be restocked." oder "Grapes are sufficiently stocked."
if shelf.count("grapes") == 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")

# Überprüfen, ob "oranges" im Tupel shelf vorhanden sind. Falls ja, deren Index ausgeben mit: "Oranges are at index: <$orange_index>". Falls sie nicht vorhanden sind, ausgeben: "Oranges are out of stock."
# Ausgabe des Index der Orangen, falls vorhanden: "Oranges are at index: <$orange_index>", oder "Oranges are out of stock."
if "oranges" in shelf:
    orange_index = shelf.index("oranges")
    print("Oranges are at index:",orange_index)
else:
    print("Oranges are out of stock.")