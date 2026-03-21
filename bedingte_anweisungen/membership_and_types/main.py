#itemName = "Strawberries"
#in_name = "Straw" in itemName
#print("Is 'Straw' in 'Strawberries'?", in_name) 




# Product details
description = "Imported honey, raw and unfiltered"
price = "5.99"
count = 120

# Write your code here
#Verwenden Sie Membership-Operatoren (in) auf dem String description:
#Überprüfen Sie, ob die Teilzeichenkette 'raw' in description enthalten ist. Speichern Sie das Ergebnis in contains_raw.
#Überprüfen Sie, ob die Teilzeichenkette 'Imported' in description enthalten ist. Speichern Sie das Ergebnis in contains_Imported.

contains_raw = "raw" in description
contains_Imported = "Imported" in description

#Verwenden Sie die Funktion type(), um die Datentypen zu überprüfen:
#Überprüfen Sie, ob price vom Typ float ist. Speichern Sie das Ergebnis in price_is_float.
#Überprüfen Sie, ob count vom Typ int ist. Speichern Sie das Ergebnis in count_is_int.

price_is_float = type(price) == float
count_is_int = type(count) == int


print("Contains 'raw':", contains_raw)
print("Contains 'Imported':", contains_Imported)
print("Is price a float?:", price_is_float)
print("Is count an integer?:", count_is_int)