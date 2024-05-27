# Saisie du nombre de valeurs
Nb = int(input("Entrez le nombre de valeurs : "))

# Redimensionnement du tableau T
T = [0] * Nb

# Saisie des valeurs dans le tableau
for i in range(Nb):
    T[i] = int(input("Entrez le nombre n° " + str(i + 1) + " : "))

# Inversion des éléments du tableau
for i in range(Nb // 2):
    T[i], T[Nb-1-i]  = T[Nb-1-i] , T[i]

    # temp = T[i]
    # T[i] = T[Nb - 1 - i]
    # T[Nb - 1 - i] = temp

# Affichage du tableau après inversion
print("Tableau après inversion :", T)