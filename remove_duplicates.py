# Beispiel Python-Skript, das doppelte Filter aus einer Liste entfernt

# Pfad zur "unified.txt"
file_path = 'filters/unified.txt'

# Filter aus der Datei lesen
with open(file_path, 'r') as f:
    filters = f.readlines()

# Duplikate entfernen
filters_set = set(filters)  # Ein Set entfernt automatisch Duplikate

# Die Liste der Filter zurück in die Datei schreiben
with open(file_path, 'w') as f:
    f.writelines(filters_set)
