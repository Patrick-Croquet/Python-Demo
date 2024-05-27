# Variable Truc en Caractère

# Début
with open("Exemple.txt", "r") as file:  # Ouvrir "Exemple.txt" sur 5 en Lecture
    Truc = file.readline().strip()  # LireFichier 5, Truc
    while Truc:  # Tantque Non EOF(5)
        print(Truc)  # Ecrire Truc
        Truc = file.readline().strip()  # LireFichier 5, Truc
# FinTantQue
# Fermer 5 (Automatiquement grâce au 'with')
# Fin