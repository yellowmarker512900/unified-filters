# Beispiel Python-Skript, das doppelte Filter aus einer Liste entfernt

# remove_duplicates.py
with open('filters/unified.txt', 'r') as f:
    filters = f.readlines()

# Entferne doppelte Filter
filters_set = set(filters)

# Schreibe die bereinigte Liste zurück in die Datei
with open('filters/unified.txt', 'w') as f:
    f.writelines(filters_set)
