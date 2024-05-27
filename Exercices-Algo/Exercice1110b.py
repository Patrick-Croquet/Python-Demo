import random

Sudok = [[0 for j in range(3)] for i in range(3)]

# Votre tableau bidimensionnel initial
tableau_bidimensionnel = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 1. Applatissez le tableau bidimensionnel en une liste unidimensionnelle
liste_unidimensionnelle = [nombre for ligne in tableau_bidimensionnel for nombre in ligne]

# 2. Mélangez la liste unidimensionnelle
random.shuffle(liste_unidimensionnelle)

# 3. Reconvertir la liste unidimensionnelle en tableau bidimensionnel
tableau_bidimensionnel_melange = [liste_unidimensionnelle[i:i+3] for i in range(0, len(liste_unidimensionnelle), 3)]

# Affichage du tableau bidimensionnel mélangé
for i in range(0, len(tableau_bidimensionnel_melange)):
    for ligne in tableau_bidimensionnel_melange:
        a = [0, 1, 2]
        b = [1, 2, 0] 
        c = [2, 0, 1]
        print(ligne[a[i]], ligne[b[i]],ligne[c[i]])
        
        
# Affichage des valeurs du tableau
# for ligne in tableau_bidimensionnel_melange:
    # print('\033[1m' '\033[95m' f" {ligne} " if ligne else '\033[0m' '\033[94m' f" {ligne} ", end="")
    # print('\033[0m' )    