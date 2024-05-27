# Déclaration du tableau Suite
Suite = [0] * 8

# Initialisation des deux premières valeurs
Suite[0] = 1
Suite[1] = 1

# Remplissage du tableau selon la formule Suite[i] = Suite[i-1] + Suite[i-2]
for i in range(2, 8):
    Suite[i] = Suite[i-1] + Suite[i-2]

# Affichage des éléments du tableau
for i in range(8):
    print(Suite[i]) # Affichage de la séquence de Fibonacci

