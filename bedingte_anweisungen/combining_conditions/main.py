# The item's discount and stock status have been defined
discounted = False
lowStock = True

# Definieren Sie eine boolesche Variable movingProduct, die True ist, wenn der Artikel entweder reduziert oder niedrig im Bestand ist, unter Verwendung von logischen Operatoren.
movingProduct = discounted or lowStock
# print("movingProduct: ",movingProduct)

# Erstellen Sie eine boolesche Variable promotion, die True ist, wenn der Artikel nicht reduziert und ausreichend auf Lager ist.
promotion = not discounted and not lowStock
# print("Promotion:", promotion)
# Geben Sie die Nachricht aus: Is the item eligible for promotion? <promotion>.
print("Is the item eligible for promotion?",promotion)