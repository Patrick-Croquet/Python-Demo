# Saisie du nombre de valeurs
Nb = int(input("Entrez le nombre de valeurs : "))

# Redimensionnement du tableau T
T = [0] * Nb

# Saisie des valeurs dans le tableau
for i in range(Nb):
    T[i] = int(input("Entrez le nombre n° " + str(i + 1) + " : "))

# Saisie du rang de la valeur à supprimer
S = int(input("Rang de la valeur à supprimer ? "))

# Suppression de la valeur à l'indice S
for i in range(S, Nb - 1):
    T[i] = T[i + 1]

# Redimensionnement du tableau après suppression
T = T[:Nb - 1]

# Affichage du tableau après suppression
print("Tableau après suppression :", T)