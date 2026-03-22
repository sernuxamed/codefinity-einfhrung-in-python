# Erstellen einer Liste meat mit den Werten: "Ham", 3.99, 50, "Sliced";
meat = ["Ham", 3.99, 50, "Sliced"]

# Erstellen einer Liste cheese mit den Werten: "Cheddar", 5.49, 100, "Sharp";
chees = ["Cheddar", 5.49, 100, "Sharp"]

# Erstellen einer Liste condiment mit den Werten: "Mustard", 1.99, 75, "Spicy".
condiment = ["Mustard", 1.99, 75, "Spicy"]

#Kombinieren der Listen meat, cheese und condiment zu einer einzigen Liste namens deli_dept.
deli_dept = [meat, chees, condiment]
print("Initial Deli List: ",deli_dept)
#print(deli_dept)

#print(meat)
#meat[2] =49
if "Ham" in meat and meat[2] < 100:
        meat[2] = 100
#print(meat)

# Erstellen einer Liste seasonal_meat mit den Werten: "Turkey", 4.50, 100, "Sliced";
# seasonal_meat an deli_dept anhängen.

seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)

#print(deli_dept)
# Würzmittel entfernen: Die Liste condiment aus deli_dept entfernen.

deli_dept.remove(condiment)
#print(deli_dept)

# Liste sortieren: deli_dept alphabetisch anhand des ersten Elements jeder Unterliste mit der Methode sort() sortieren.
deli_dept.sort()
#print(deli_dept)

# Den Anfangszustand von deli_dept mit der Nachricht ausgeben: "Initial Deli List: <$deli_dept>".
# Nach allen Operationen den aktualisierten Zustand von deli_dept mit der Nachricht ausgeben: "Updated Deli List: <$deli_dept>".
print("Updated Deli List: ",deli_dept)