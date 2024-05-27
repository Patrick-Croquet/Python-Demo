# Déclaration du tableau Truc
Truc = [[0 for j in range(13)] for i in range(6)]

# Initialisation du tableau à zéro
for i in range(6):
    for j in range(13):
        Truc[i][j] = 0

for ligne in Truc:
    print(ligne)