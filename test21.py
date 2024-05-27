import csv

# Données structurées (enregistrements)
enregistrements = [
    {'nom': 'Alice', 'age': 30, 'ville': 'Paris'},
    {'nom': 'Bob', 'age': 25, 'ville': 'Lyon'},
    {'nom': 'Charlie', 'age': 35, 'ville': 'Marseille'}
]

# Écriture des enregistrements dans un fichier CSV
with open('donnees.csv', 'w', newline='') as fichier:
    writer = csv.DictWriter(fichier, delimiter=';', fieldnames=['nom', 'age', 'ville'])
    writer.writeheader()
    writer.writerows(enregistrements)