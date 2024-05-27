# Déclaration du tableau X
X = [[0 for j in range(3)] for i in range(2)]

# Initialisation des valeurs du tableau
val = 1
for i in range(2):
    for j in range(3):
        X[i][j] = val
        val += 1

# Affichage des valeurs du tableau
for i in range(2):
    for j in range(3):
        # print(f"X({i}, {j}) = {X[i][j]}")
        print("X[{}, {}] = {}".format(i, j, X[i][j]))

for ligne in X:
    print(ligne)