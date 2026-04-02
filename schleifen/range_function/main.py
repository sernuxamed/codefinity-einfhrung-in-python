# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

#start: Dies ist die erste Zahl der Sequenz. Sie ist optional; wenn sie nicht angegeben wird, beginnt die Sequenz bei 0.
#stop: Dies ist die letzte Zahl der Sequenz, aber die Sequenz endet direkt vor dieser Zahl. Dieses Argument ist erforderlich.
#step: Dies ist der Wert, um den zwischen den Zahlen erhöht (oder verringert) wird. Er ist optional; wenn er nicht angegeben wird, erhöht sich die Sequenz jeweils um 1.


#Verwenden Sie zwei Listen — weekdays und daily_promotions —, um die jeweils zugewiesene Aktion für jeden Wochentag auszugeben.
for i in range(len(weekdays)):
    day = weekdays[i]
    promo = daily_promotions[i]
    print(day," : Promotion on ",promo)