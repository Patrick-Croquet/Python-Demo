# Demande à l'utilisateur d'entrer le nombre de valeurs
Nb = int(input("Entrez le nombre de valeurs : "))

# Redimensionnement du tableau T
T = [0] * Nb

# Lecture des valeurs
for i in range(Nb):
    T[i] = int(input("Entrez le nombre n° " + str(i + 1) + " : "))

# Affichage du nouveau tableau
print("Nouveau tableau :")
for i in range(Nb):
    T[i] += 1
    print(T[i])
