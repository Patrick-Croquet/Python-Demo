import csv

# Lecture des données structurées à partir d'un fichier CSV
with open('donnees.csv', 'r') as fichier:
    reader = csv.DictReader(fichier, delimiter=';')
    for row in reader:
        if row['nom'] == 'Bob' :
            break

print(row['nom'], row['age'], row['ville'])