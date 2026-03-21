seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

# Definieren Sie eine boolesche Variable overstock_risk als True, wenn der Artikel seasonal ist und sein current_stock den high_stock_threshold überschreitet.
overstock_risk = seasonal and current_stock > high_stock_threshold
#print(overstock_risk)

# Definieren Sie eine weitere boolesche Variable discount_eligible als True, wenn der Artikel sich not selling_well verkauft und sich not bereits on_sale befindet.
discount_eligible = not selling_well and not on_sale
# print(discount_eligible)

# Erstellen Sie eine boolesche Variable make_discount, die True ist, wenn entweder overstock_risk oder discount_eligible True ist.
make_discount = overstock_risk or discount_eligible
#print(make_discount)

print("Should the item be discounted?",make_discount)