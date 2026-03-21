# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

#Schneiden Sie den String items, um zu extrahieren:
candy1 = items[0:9]
#print(candy1)
candy2 = items[11:20]
#print(candy2)
dry_goods = items[22:27]
#print(dry_goods)

#Schneiden Sie den String categories, um zu extrahieren:
category1 = categories[0:11]
#print(category1)
category2 = categories[13:24]
#print(category2)

# Erstellen Sie Preisvariablen
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"
#print(bubblegum_price)
#print(chocolate_price)
#print(pasta_price)

# Verwenden Sie print(), um Artikelnamen, Preise und Kategorien anzuzeigen.

print("We have " +candy1+ " for "+bubblegum_price+" in the "+category1+" .")
print()
print("We have " +candy2+ " for "+chocolate_price+" in the "+category1+" .")
print()
print("We have " +dry_goods+ " for "+pasta_price+" in the "+category2+" .")