# Déclaration du tableau N
N = [0] * 7

# Initialisation de la première valeur
N[0] = 1

# Remplissage du tableau selon la formule N[k] = N[k-1] + 2
for k in range(1, 7):
    N[k] = N[k-1] + 2

# Affichage des éléments du tableau
for i in range(7):
    print(N[i])