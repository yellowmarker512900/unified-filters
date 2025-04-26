# Beispiel Python-Skript, das doppelte Filter aus einer Liste entfernt

# remove_duplicates.py
with open('filters/essentials.txt', 'r') as f:
    filters = f.readlines()

# Entferne doppelte Filter
filters_set = set(filters)

# Schreibe die bereinigte Liste zurück in die Datei
with open('filters/essentials', 'w') as f:
    f.writelines(filters_set)
