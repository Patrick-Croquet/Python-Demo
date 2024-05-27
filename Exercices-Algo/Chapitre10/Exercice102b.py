# Début
with open("Exemple.txt", "r") as file:  # Ouvrir "Exemple.txt" sur 5 en Lecture
    for line in file: 
        modified_line = line.replace('/', '')                
        print(modified_line, end='')   

# Fermer 5 (Automatiquement grâce au 'with')
# Fin