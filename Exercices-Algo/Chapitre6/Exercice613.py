# Demande à l'utilisateur d'entrer le nombre de valeurs
Nb = int(input("Entrez le nombre de valeurs : "))

# Redimensionnement du tableau T
T = [0] * Nb

# Lecture des valeurs
for i in range(Nb):
    T[i] = float(input("Entrez le nombre n° " + str(i + 1) + " : "))

# Recherche de l'élément le plus grand et de sa position
Posmaxi = 0
for i in range(1, Nb):
    if T[i] > T[Posmaxi]:
        Posmaxi = i

# Affichage de l'élément le plus grand et de sa position
print("Element le plus grand :", T[Posmaxi])
print("Position de cet élément :", Posmaxi)