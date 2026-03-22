# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]

#Umwandlung der Liste shelf1_update in ein Tupel mit dem Namen shelf1_update_tuple.
shelf1_update_tuple = tuple(shelf1_update)

#Verkettung von shelf1_update_tuple mit dem bestehenden Tupel shelf1, um ein neues Tupel namens shelf1_concat zu erstellen
shelf1_concat = (shelf1_update_tuple, shelf1)
print(shelf1_concat)

#Zählen, wie oft der String "celery" in shelf1_concat vorkommt, und Speichern dieser Anzahl in einer Variablen namens celery_count.
celery_count = shelf1_concat.count("celery")
print(celery_count)