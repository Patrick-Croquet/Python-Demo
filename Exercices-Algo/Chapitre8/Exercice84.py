# Déclaration du tableau T
T = [[0 for m in range(2)] for k in range(4)]

# Initialisation des valeurs du tableau
for k in range(4):
    for m in range(2):
        T[k][m] = k + m

# Affichage des éléments de T
for k in range(4):
    for m in range(2):
        print("T[{}, {}] = {}".format(k, m, T[k][m]))