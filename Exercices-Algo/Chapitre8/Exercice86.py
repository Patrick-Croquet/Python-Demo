# Déclaration du tableau T
T = [[0 for j in range(9)] for i in range(13)]

# Initialisation des valeurs du tableau (à titre d'exemple)
for i in range(13):
    for j in range(9):
        T[i][j] = i * j  # Exemple d'initialisation

# Recherche du plus grand élément
iMax = 0
jMax = 0
for i in range(13):
    for j in range(9):
        if T[i][j] > T[iMax][jMax]:
            iMax = i
            jMax = j

# Affichage du plus grand élément et de ses indices
print("Le plus grand élément est", T[iMax][jMax])
print("Il se trouve aux indices", iMax, ";", jMax)