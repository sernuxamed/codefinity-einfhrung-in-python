start_number = 5
countdown_values = []

#Verwendung einer while-Schleife, um von start_number bis 1 (einschließlich) herunterzuzählen, wobei in jeder Iteration um 1 dekrementiert wird.
while start_number > 0:
#    print(start_number)
    countdown_values.append(start_number)
#    print(countdown_values)
    start_number -= 1

print("Discount countdown complete!",countdown_values)